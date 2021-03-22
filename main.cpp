#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <string>
#include <thread>
#include <vector>
#include <mutex>

#include "md5.h"
#include "sha256.h"

using namespace std;

vector<string>  words;
vector<string>  hashedWord;

mutex hashMtx;
bool hashThreadComp = false;
bool stopHashThread = false;
int tSize = 0;

void showHelp();

void hashThread(string args) {
    if (args == "md5") {
        for (int e = 0; e < words.size(); e++) {
            hashMtx.lock();
            hashedWord.push_back(md5(words[e]));
            tSize++;
            if (stopHashThread) {
                hashMtx.unlock();                   
                return;
            }
            hashMtx.unlock(); 
        }
    } else if (args == "sha256") {
        for (int e = 0; e < words.size(); e++) {
            hashMtx.lock();
            hashedWord.push_back(sha256(words[e]));
            tSize++;
            if (stopHashThread) {
                hashMtx.unlock();
                return;
            }
            hashMtx.unlock();
        }
    };
    hashMtx.lock();
    hashThreadComp = true;
    hashMtx.unlock();
}


int main(int argc, char* argv[]) {
    vector<string>  fails;
    bool cracked;

    if (argc == 1) {
        showHelp();
    } else {
        thread hashThreadMethod;
        for (int i = 1; i < argc; i++) {
            string str_args = string(argv[i]);
            if (str_args == "-wL") {
                i++;
                if (i >= argc) {
                    cout << "E: An argument was expected for " << argv[i - 1] << endl;
                    return 0;
                }

                fstream file;
                file.open(argv[i], ios::in);
                if (file.is_open()) {
                    string word;
                    while (file >> word)
                        words.push_back(word);
                } else {
                    cout << "E: File / Directory " << argv[i] << " Does not exist" << endl;
                    return 0;
                }
            } else if (str_args == "-hT") {
                i++;
                if (i >= argc) {
                    cout << "E: An argument was expected for " << argv[i - 1] << endl;
                    return 0;
                }

                string str_args_mode = string(argv[i]);
                string args_lower = string(argv[i]);
                transform(args_lower.begin(),
                        args_lower.end(), 
                        args_lower.begin(), 
                        ::tolower);

                hashThreadMethod = thread(hashThread, args_lower);
            } else if (str_args == "-h") {
                i++;
                string hash = argv[i];
                int denominator = 0;
                while (!hashThreadComp && denominator != words.size()) {
                    if (denominator + 1 <= hashedWord.size()) {
                        if (hash == hashedWord[denominator]) {
                            stopHashThread = true;
                            hashThreadMethod.join();   

                            cout << "Failed password count: " << fails.size() << endl;
                            cout << hash << " : [ =!=!=!= ] : " << words[denominator] << endl;
                            cracked = true;

                            break;
                        } else {
                            fails.push_back(words[denominator]);
                        } denominator++;
                    }
                }
                if (fails.size() == words.size()) {
                    cout << "Failed to find password within provided list." << endl;
                    stopHashThread = true;
                    hashThreadMethod.join();
                }
            } else if (str_args == "--help") {
                showHelp();
            } else {
                cout << "Invalid argument: " << argv[i] << endl;
            }
        }
    }
}


void showHelp() {
    cout << R"(
     /$$$$$$  /$$                         /$$                 /$$   /$$                     /$$      
    /$$__  $$|__/                        | $$                | $$  | $$                    | $$      
    |$$  \__/ /$$ /$$$$$$/$$$$   /$$$$$$ | $$  /$$$$$$       | $$  | $$  /$$$$$$   /$$$$$$$| $$$$$$$ 
    | $$$$$$ | $$| $$_  $$_  $$ /$$__  $$| $$ /$$__  $$      | $$$$$$$$ |____  $$ /$$_____/| $$__  $$
    \____  $$| $$| $$ \ $$ \ $$| $$  \ $$| $$| $$$$$$$$      | $$__  $$  /$$$$$$$|  $$$$$$ | $$  \ $$
    /$$  \ $$| $$| $$ | $$ | $$| $$  | $$| $$| $$_____/      | $$  | $$ /$$__  $$ \____  $$| $$  | $$
    | $$$$$$/| $$| $$ | $$ | $$| $$$$$$$/| $$|  $$$$$$$      | $$  | $$|  $$$$$$$ /$$$$$$$/| $$  | $$
    \______/ |__/|__/ |__/ |__/| $$____/ |__/ \_______/      |__/  |__/ \_______/|_______/ |__/  |__/
                               | $$                                                                  
                               | $$                                                                  
                               |__/                                                                  

    )"
        << endl
        << "----Help:-----------------------------"
        << endl
        << "--help |   Open Help menu\n"
        "       |   usage: shash -h"
        << endl
        << "--------------------------------------"
        << endl
        << "-wL    |   Enter wordlist location\n"
        "       |   usage: shash -wL <filename>"
        << endl
        << "--------------------------------------"
        << endl
        << "-hT    |   Select hash type\n"
        "       |   usage: shash -hT <hash type>"
        << endl
        << "--------------------------------------"
        << endl
        << "-m     |   Enter mode\n"
        "       |   usage: shash -m <mode>"
        << endl;
}

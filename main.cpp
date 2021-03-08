#include <iostream>
#include <fstream>
#include <string>
#include <bits/stdc++.h>

#include "md5.h"
#include "sha256.h"

using namespace std;

void showHelp();

int main(int argc, char *argv[])
{
    vector<string>  words;
    vector<string>  hashed_word;
    vector<string>  fails;
    bool cracked;

    if (argc == 1)
    {
        showHelp();
    }
    else
    {
        for (int i = 1; i < argc; i++)
        {
            string str_args = string(argv[i]);
            if (str_args == "-wL")
            {
                i++;

                if (i >= argc)
                {
                    cout << "E: An argument was expected for " << argv[i - 1];
                    return 0;
                }

                fstream file;
                file.open(argv[i], ios::in);
                if (file.is_open())
                {
                    string word;

                    while (file >> word)
                    {
                        words.push_back(word);
                    }
                }
                else
                {
                    cout << "E: File / Directory " << argv[i] << " Does not exist";
                    return 0;
                }
            }
            else if (str_args == "-m")
            {
                i++;

                if (i >= argc) {
                    cout << "E: An argument was expected for " << argv[i - 1];
                    return 0;
                }

                string str_args_mode = string(argv[i]);
                string args_lower = string(argv[i]);

                transform(args_lower.begin(), args_lower.end(), args_lower.begin(), ::tolower);

                if (args_lower == "md5") {
                    for (int e = 0; e < words.size(); e++) {
                        hashed_word.push_back(md5(words[e]));
                    }
                } else if (args_lower == "sha256") {
                    for (int e = 0; e < words.size(); e++) {
                        hashed_word.push_back(sha256(words[e]));
                    }
                }
            }
            else if (str_args == "-h") {
                i++;

                string hash = argv[i];

                for (int d = 0; d < words.size(); d++) {
		    if (hash == hashed_word[d]) {
                cout << "Failed password count: " << fails.size() << "\n";
                cout << hash << " : [ =!=!=!= ] : " << words[d];
                cracked = true;
			    break;
		    } else {
			    fails.push_back(words[d - 1]);
		    }
		}
                if (fails.size() == words.size()) {
                    cout << "Failed to find password within provided list." << endl;
                }
            }
            else if (str_args == "--help")
            {
                showHelp();
            }
            else
            {
                cout << "Invalid argument: " << argv[i];
            }
        }
    }
}

void showHelp()
{
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
         << "-m     |   Enter mode\n"
            "       |   usage: shash -m <mode>"
         << endl;
}

#include <iostream>
#include <fstream>
#include <string>

#include "md5.h"

using namespace std;

void showHelp();

int main(int argc, char* argv[]) {

    cout << md5("Hello World!");

    if (argc == 1) {
        showHelp();
    } else {
        // int args_count = sizeof(arguments) / sizeof(arguments[0]);
        for (int i = 1; i < argc; i++) {
            string str_args = string(argv[i]);
            if (str_args == "-f") {
                i++;

                if (i >= argc) {
                    cout << "E: An argument was expected for " << argv[i - 1];
                }

                fstream file;
                file.open(argv[i], ios::in);
                if (file.is_open()) {
                    string tp;
                    while (getline(file, tp)) {
                        cout << tp << "\n";
                    }
                    file.close();
                } else {
                    cout << "E: File / Directory " << argv[i] << " Does not exist";
                }
            } else if (str_args == "-m") {
                i++;

            } else if (str_args == "-h") {
                showHelp();
            }
        }
    }
}

void showHelp() {
    cout <<
         "Simple Hash\n"
         << endl <<
         "----Help:-----------------------------"
         << endl <<
         "-h   |   Open Help menu\n"
         "     |   usage: shash -h"
         << endl <<
         "--------------------------------------"
         << endl <<
         "-f   |   Enter wordlist location\n"
         "     |   usage: shash -f <filename>"
         << endl <<
         "--------------------------------------"
         << endl <<
         "-m   |   Enter mode\n"
         "     |   usage: shash -m <mode>"
         << endl;
}
#include <cctype>
#include <fstream>
#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
    unsigned int sum = 0;
    string line;

    const std::map<std::string, int> value_map = {
            {"one",   1},
            {"two",   2},
            {"three", 3},
            {"four",  4},
            {"five",  5},
            {"six",   6},
            {"seven", 7},
            {"eight", 8},
            {"nine",  9}
    };

    // for every line calculate the calibration code and sum up
    ifstream infile("./input.txt");
    while (getline(infile, line)) {
        bool already_first = false;
        int  last_num = 0;

        for (int i = 0; i < (int)line.size(); i++) {
            if (std::isdigit(line[i])) {
                if (!already_first) {
                    sum           += 10 * (line[i] - '0');
                    already_first  = true;
                }
                last_num = line[i] - '0';
            } else {
                int num = 0;
                for (auto &[key, val] : value_map) {
                    if (line.substr(i, key.size()) == key) {
                        num = val;
                        break;
                    }
                }

                // if we didn't find a correct value we will
                // continue to next iteration
                if (num == 0)
                    continue;

                if (!already_first) {
                    sum           += 10 * num;
                    already_first  = true;
                }
                last_num = num;
            }
        }

        sum += last_num;
    }
    infile.close();

    // print result
    cout << "sum equals " << sum << endl;

}
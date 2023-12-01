#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int concat(int a, int b)
{

    // Convert both the integers to string
    string s1 = to_string(a);
    string s2 = to_string(b);

    // Concatenate both strings
    string s = s1 + s2;

    // Convert the concatenated string
    // to integer
    int c = stoi(s);

    cout << "sum line : " << c << endl;

    // return the formed integer
    return c;
}
int main() {
    int sum = 0;

    // Open the file using ifstream
    std::ifstream file("C:/Users/mitue/Documents/Perso/code/Advent_of_code_2023/Day_1/input.txt");

    // Check if the file is opened successfully
    if (!file.is_open()) {
        std::cerr << "Unable to open the file." << std::endl;
        return 1; // Return an error code
    }

    // Read the file line by line
    std::string line;
    while (std::getline(file, line)) {
        int number1 = 0;
        int number2 = 0;

        // Check if the character is a number
        for (int i = 0; i < line.length(); i++) {
            if (isdigit(line[i])) {
                if (number1 == 0) {
                    number1 = line[i] - '0';
                }
            }
        }
        for (int i = line.length() - 1 ; i >= 0; i--) {
            if (isdigit(line[i])) {
                if (number2 == 0) {
                    number2 = line[i] - '0';
                }
            }
        }

        sum += concat(number1, number2);
    }

    // Close the file
    file.close();

    std::cout << "Final sum is equal to " << sum << std::endl;
    return 0;
}

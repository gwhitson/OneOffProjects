#define CHARS_IN_PAGE 8400000

#include <cstdlib>
#include <iostream>
#include <array>
#include <random>
#include <fstream>


std::array<char, 29> chars = {'a','b','c','d','e','f','g','h','i','j','k','l','m',
                              'n','o','p','q','r','s','t','u','v','w','x','y','z',
                              '.',',',' '};

int main(int argc, char *argv[]){
    if (argc != 2) {
        std::cerr << "Usage: must supply string to search for" << std::endl;
        return 127;
    //} else {
    //    std::cout << argv[1] << std::endl;
    //    return 0;
    }
    std::string str = "";
    do {
        std::random_device dev;
        std::mt19937 rng(dev());
        std::uniform_int_distribution<std::mt19937::result_type> dist29(1,29);
        std::ofstream page;
        str = "";
        page.open("page.txt");
        int count = 0;
        do {
            int ran = dist29(rng);
            str += chars[ran];
            //page << chars[ran];
            count++;
        } while (count < CHARS_IN_PAGE);
        page << str;
        page.close();
        std::cout << "generated page" << std::endl;
        std::cout << str << std::endl;
    } while (str.find(argv[1]) == str.npos)  ;
}

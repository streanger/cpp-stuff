// basic file operations
#include <iostream>
#include <fstream>
#include <time.h>
#include <string>
using namespace std;
string now();

int main () {
    std:string current_time = now();
    ofstream myfile;
    myfile.open ("example.txt");
    myfile << "Writing this to a file.\n";
    myfile << current_time;
    myfile.close();
    return 0;
}

string now ()
{
    time_t theTime = time(NULL);
    struct tm *aTime = localtime(&theTime);

    int day = aTime->tm_mday;
    int month = aTime->tm_mon + 1; // Month is 0 – 11, add 1 to get a jan-dec 1-12 concept
    int year = aTime->tm_year + 1900; // Year is # years since 1900
    int hour=aTime->tm_hour;
    int min=aTime->tm_min;
    std:string current_time;
    // fastformat::fmt(result, "time: {0}:{1}", hour, min);
    current_time = std::to_string(hour) + ":" + std::to_string(min);    
    return current_time;
}


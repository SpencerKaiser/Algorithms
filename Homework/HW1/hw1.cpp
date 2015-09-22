#include <iostream>
#include <tgmath.h>
#include <ctime>

using namespace std;

float performCalculation(){
    //Create start/stop vals for caluclation
    float initialVal = 1.0, endVal = 2.0;
    
    //Create variables for sum and x
    float totalSum = 0.0, x = initialVal;
    
    //Iterate through all possible values for x from startVal to endVal
    while (x < endVal) {
        totalSum += (1/x);
        
        //Increase value of x with smallest possible value for float type
        x = nextafterf(x, endVal);
    }
    
    return totalSum;
}

int main(){
    clock_t startTime = clock();            //Start clock
    float sum = performCalculation();       //Perform calculation
    clock_t endTime = clock();              //End clock
    
    //Print results
    cout << "Sum: " << sum << endl;
    cout << "Total Time: " << (endTime - startTime)/ (double)(CLOCKS_PER_SEC / 1000) << "ms" << endl;
}
#include <iostream>
#include <cmath>
#include <iomanip>
#include <sys/time.h>
#include <cstdlib>

/**
  * You are to implement and test a program for summing 1/x as x runs 
  * over all approximately eight million (23 fraction bits) single precision 
  * floating point numbers in the interval [1, 2). You are to do this on a 
  * server, PC (or Mac) of your choice. You are first asked to predetermine 
  * estimates of your implementation’s computation time (architecture and 
  * compiler dependant), result accuracy (algorithm and round-off dependant), 
  * and result value (real valued sum estimate).
  */

#ifdef __i386
__inline__ uint64_t rdtsc() {
      uint64_t x;
        __asm__ volatile ("rdtsc" : "=A" (x));
          return x;
}
#elif __amd64
__inline__ uint64_t rdtsc() {
      uint64_t a, d;
        __asm__ volatile ("rdtsc" : "=a" (a), "=d" (d));
          return (d<<32) | a;
}
#endif

void testCycleTimes() {
    float x = 1.0;
    uint64_t t = rdtsc();
    x = nextafterf(x, 10.0);
    t = rdtsc() - t;
    std::cout << "Clock cycles for nextafterf:  " << t << std::endl;

    t = rdtsc();
    x = 1/x;
    t = rdtsc()-t;
    std::cout << "Clock cycles for division: " << t << std::endl;
}

int main() {

    testCycleTimes();
    const float maxValue = 2.0;
    const double expectedSum = 592405.333333;
    float x = 1.0;
    double sum = 0.0;

    int count = 0;
    timeval startTime, endTime;

    gettimeofday(&startTime, NULL); // Get the current time

    while (x < maxValue) {
        sum += (1/x);
        x = nextafterf(x, 10.0); //Move to next floating point value
        ++count;
    }

    gettimeofday(&endTime, NULL); // Get the time after all computation is complete

    double runTime = ((double)endTime.tv_usec) - ((double)startTime.tv_usec);

    std::cout << "Total number of additions: " << count << std::endl;
    std::cout << "Sum of all 1/x in [1,2) : " << std::setprecision(20) << sum << std::endl;
    std::cout << "Run time in microseconds: " << std::setprecision(20) << runTime << std::endl;
    std::cout << "Error in actual sum: " << std::setprecision(20) << ((sum - expectedSum)/expectedSum) << std::endl;
    std::cout << "\n" << std::endl;
}

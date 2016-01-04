import time
import numpy as np


def performSummation():
    # Instantiate summation range values
    start_val = np.float32(1.0)
    end_val = np.float32(2.0)

    sum = 0.0
    x = start_val
    # num_vals = 0

    while(x < end_val):
        sum += 1/x
        x = np.nextafter(x, end_val)
    # num_vals += 1
    return sum




def main():
    # Get start time of execution
    start_time = time.time()

    # Perform Summation calculations
    sum = performSummation()
    
    # Get end time of execution
    end_time = time.time()
    
    print("SUM: %s" % sum)
    
    # Calculate total execution time
    print("Execution Time: %s" % (end_time - start_time))


main()
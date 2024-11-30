#cacheless verison. run with terminal - instructions in readme file 


import os
import math
import argparse
import sys
import time

counter_cacheless = 0


# Curtis Van Ausdal
#noncache version
import os
import math

import argparse
import time

counter_cacheless = 0


# CALCULATES THE SHOULDER WEIGHT PERSON IN (ROW,COL) IS BEARING ON TOP OF THEM (THEIR OWN WEIGHT EXCLUDED): I. E : "SHOULDER WEIGHT".
def weight_on_cacheless(row, col):
    global counter_cacheless
    counter_cacheless += 1

    if row == 0:  # very top peice of pyramid
        result = 0



    elif col == 0:  # left side
        result = (200 / 2) + ((weight_on_cacheless(row - 1, 0)) / 2)



    elif col == row:  # right side
        result = (200 / 2) + (weight_on_cacheless(row - 1, col - 1) / 2)



    else:  # covers the middle rows
        result = 200 + (weight_on_cacheless(row - 1, col - 1) + weight_on_cacheless(row - 1,
                                                                                    col)) / 2  # BEWARE TO WRITER: adding 200 made it work but I'm not sure why. My brain says to add 100 but it didn't work

    return result


print(weight_on_cacheless(0,0))
# print(counter)


# Part 3 -- Write weight_on_with_caching() method
def weight_on_with_caching(r,c):
    pass

def main():

    parser = argparse.ArgumentParser(description="ROWS")
    parser.add_argument('rows', type=int, help="number of rows to calculate")
    args = parser.parse_args()

    # takes given rows and spits out the shoulder weight of everyone in range of given row. prints information and
    # also writes it to file called part2.out
    outfile = open('cacheless.txt', 'w')
    start = time.perf_counter()

    for row in range(args.rows):
        print('\n')
        outfile.write(f'\n')

        for col in range(row + 1):
            # print('', round(weight_on_cacheless(row, col),2), end = '',) #just in case f string method fails, this works too
            shoulder_data = f'    {weight_on_cacheless(row, col):.2f} '
            print(shoulder_data, end=' ')

            outfile.write(f'{shoulder_data}')

    end = time.perf_counter()
    # print('')
    time_elapsed = end - start  # end timer and fine time elapsed
    print('\n')
    print(f'Elapsed time:  {time_elapsed} seconds')  # print time elapsed to console
    print(f'number of function calls: {counter_cacheless}')

    # write the time and function calls to file
    outfile.write('')
    # outfile.write('\n')
    outfile.write('\n')
    outfile.write(f'	Elapsed time:  {time_elapsed} seconds \n')
    outfile.write(f'	number of function calls: {counter_cacheless} \n')
    outfile.close()
# close the file and part 2 is finished!
if __name__ == '__main__':
    main()
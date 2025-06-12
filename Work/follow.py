# follow.py
#
# Exercise 8.1

import os
import time

def follow(filename):
    '''
    Generator that produces a sequence of lines being written at the end of a file.
    '''
    with open(filename, 'r') as f:
        f.seek(0, os.SEEK_END)    # Move file pointer 0 bytes from end of file
        while True:
            line = f.readline()
            if line =='':
                time.sleep(0.1)    # Sleep briefly and retry
                continue
            yield line

if __name__ == '__main__':
    for line in follow('../Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print('%10s %10.2f %10.2f' % (name, price, change))
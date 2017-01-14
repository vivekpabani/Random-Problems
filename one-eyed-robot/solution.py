#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import time


def swap(a_balls, i, j):

    a_balls[i], a_balls[j] = a_balls[j],  a_balls[i]
    return


def main():

    start_time = time.clock()
    balls = ['G', 'B', 'R', 'R', 'B', 'G', 'R', 'B']

    length = len(balls)

    p1, p2, p3 = 0, 0, length-1

    while p2 < p3:
        if balls[p2] == 'G':
            p2 += 1

        elif balls[p2] == 'R':
            swap(balls, p1, p2)
            p2 += 1
            p1 += 1
        
        elif balls[p2] == 'B':
            swap(balls, p2, p3)
            p3 -= 1
        
        else:
            print("Error\n")
            break
        
    print(balls)

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))


if __name__ == '__main__':
    main()






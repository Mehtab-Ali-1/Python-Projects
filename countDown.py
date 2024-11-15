# Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 and then output Liftoff!

# Here's a sample run of the program:

# 10 9 8 7 6 5 4 3 2 1 Liftoff!

# There are many ways to solve this problem. One approach is to use a for loop, and to use the for loop variable i. Recall that i will keep track of how many times the for loop has completed executing its body. As an example this code:

# for i in range(10): print(i)

# Will print out the values 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. The values printed in liftoff are 10 minus the number of times the for loop has completed.


def CountDown():
    for i in range(10, -1, -1):
        print(i,end=" ");
    print("  Liftoff!");
CountDown();
# *********************************************************
array_list :list[int] =[10,9,8,7,6,5,4,3,2,1,0];
def CountDown1():
    for i in array_list:
        print(i, end=" ");
    print("  Liftoff!");
CountDown1();
    
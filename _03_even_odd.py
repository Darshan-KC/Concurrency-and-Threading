# Write a python program to create two threads to find even and odd from 30 to 50

import threading
def even():
    print("Even numbers from 30 to 50 are")
    for i in range(30,51,2):
        print(i,end=" ")
    
def odd():
    print("Odd numbers from 30 to 50 are")
    for i in range(31,50,2):
        print(i,end=" ")
        
    
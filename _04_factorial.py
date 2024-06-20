#Write a python program to calculate the factorial of a number using multiple threads

import threading

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1)

def calculate_factorial(n,name):
    thread1 = threading.current_thread().name=name
    print(f"\nCalculation the factorial of {n} in thread {thread1}")
    result = factorial(n)
    print(f"The factorial of {n} is {result} in thread {thread1}")

def main():
    n1=5
    n2=10
    
    # Create threads for factorial calculation
    thread1 = threading.Thread(target=calculate_factorial, args=(n1,"Thread1"))
    thread2 = threading.Thread(target=calculate_factorial, args=(n2,"Thread2"))
    
    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for the threads to complete
    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()
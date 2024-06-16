# Write a python program to create multiple threads and print their names
import threading

def print_name():
    print("Thread name is ",threading.current_thread().name)
    
def main():
    # creating multiple threads
    threads = []
    
    # thread = threading.Thread(target=print_name,name="Ram") -> you can give name of thread using name
    for i in range(6):
        thread = threading.Thread(target=print_name)
        threads.append(thread)
        
        # starting thread
        thread.start()
        
    # joining threads to wait for their completion
    for thread in threads:
        thread.join()
        
    # Main thread
    print("Current thread name:", threading.current_thread().name)
    
if __name__ == "__main__":
    main()
    
# Note:
# Main Thread: This is the initial thread that starts when the program runs. It executes the main part of your script. It is the thread that runs the main code of your script and is implicitly created by the Python interpreter when you start your program.

# Additional Threads: These are created using the threading.Thread class and run concurrently with the main thread.
    
    

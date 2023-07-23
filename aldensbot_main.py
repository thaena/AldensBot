import time, os, gc
from os import system
from random import randint

# Terminal title
system("title " + "AldensBot")

# Directory
directory_path = os.path.dirname(os.path.abspath(__file__))

print("Connecting to Reddit...\n")

while True:

    try:

        # Opens notification.py
        with open(os.path.join(directory_path, 'notification.py')) as file:
            # Runs notification.py
            exec(file.read()) # runs
            file.close() # Closes file
        
        # Forces garbage collection to prevent memory leak
        gc.collect()

    # Prints on exception
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(randint(600, 780))
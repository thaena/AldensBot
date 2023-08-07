import time, os
from os import system
from random import randint

# Terminal title
system("title " + "AldensBot")

# Directory
directory_path = os.path.dirname(os.path.abspath(__file__))

print("Connecting to Reddit...\n")

while True:
    try:
        # notification.py
        with open(os.path.join(directory_path, "notification.py")) as file:
            exec(file.read())
            file.close()

    except Exception as e:
        print(f"Error: {e}")

    time.sleep(randint(600, 780))

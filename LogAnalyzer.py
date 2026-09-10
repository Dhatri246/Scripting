import os
from pathlib import Path

file = input("Enter a valid file path: ")

if os.path.exists(file):
    text = open(file).read()
    print(text)

else:
    print("File does not exist!") 

    
import os
from pathlib import Path

def checkPath(file_path):
    if os.path.exists(file_path):
        readFile(file_path)
    else:
        print("File does not exist!")   


def readFile(file_path):

    file = open(file_path).read()
    print(file)
    

def main():
    file_path = input("Enter a valid file path: ")
    checkPath(file_path)
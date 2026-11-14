import os
import argparse
from dataclasses import dataclass


def check_path(file_path):

    if os.path.exists(file_path):
        read_file(file_path)
    else:
        print("File does not exist!")   


def read_file(file_path):

    with open(file_path, "r") as file:
    #file = open(file_path).read()
    # Using 'with' ensures the file is safely closed after reading
        for line in file:
            if "error" in line.lower():
                print(line.strip())
            # else:
            #     print("no error")       #debug
    

def main():
    
    # file_path = input("Enter a valid file path: ")
    # check_path(file_path)

    parser = argparse.ArgumentParser(description = "Scan and filter log files.") 
  
    parser.add_argument("-f", "--filepath", required=True, help="path to log file")

    args = parser.parse_args()             

    check_path(args.filepath)




if __name__ == "__main__": 
    main()



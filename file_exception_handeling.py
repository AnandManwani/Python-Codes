#!/usr/bin/env python3
def file_operation(fname):
    try:
        file = open(fname).read()
        print(int(file))
        print("Thank you for using our program")
         

    except FileNotFoundError:
        print ("File " + fname + " not found.")
    except ValueError:
            print("File " + fname + " contains invalid salary")


if __name__ == "__main__":
        file_name = input()
        file_operation(file_name)
        
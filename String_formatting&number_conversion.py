#print number into decimal , octal, binary, hexadecimal in python
def print_formatted(number):
    # your code goes here
    for i in range(1, number+1):
        
        b = str("{0:b}".format(number))
        
        print(str(i).rjust(len(b)) + str("{0:o}".format(i)).rjust(len(b)+1) + str("{0:X}".format(i)).rjust(len(b)+1) + str("{0:b}".format(i)).rjust(len(b)+1))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
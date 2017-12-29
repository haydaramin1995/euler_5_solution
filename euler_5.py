
# REQUIRES: num integer after 2520
# EFFECTS: returns true if integer is divisable by numbers in range 1:20
# returns false if integer isn't divisible by any of the numbers
def verify(num):
    if(num % 18 != 0):
        return False
    if(num % 16 != 0):
        return False
    if(num % 20 != 0):
        return False
    if(num % 15 != 0):
        return False
    if(num % 14 != 0):
        return False
    if(num % 11 != 0):
        return False
    if(num % 13 != 0):
        return False
    if(num % 19 != 0):
        return False
    if(num % 17 != 0):
        return False
    return True

def main():
    i = 2520
    while(not verify(i) ):
        i = i + 2
    print(i)

if __name__ == "__main__":
    main()

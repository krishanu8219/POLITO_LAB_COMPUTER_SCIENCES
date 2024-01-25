def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a    


def main():

    gcdRunning = 0

    while True:
        value = int(input("Enter the positive values one at a time (to stop enter 0 or a negative value) :"))
        if value == 0 or value < 0:
            break
        
        if gcdRunning == 0:
            gcdRunning  = value
        else:
            gcdRunning = gcd(gcdRunning, value)    

    print(f"The GCD of the given sequence is {gcdRunning}")

if __name__ == "__main__":
    main()    
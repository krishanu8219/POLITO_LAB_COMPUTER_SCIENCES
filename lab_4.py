def main():
    first_element = int(input("Enter the value for x1: "))
    second_element = int(input("Enter the value for x2: "))

    b = [first_element,second_element]
     
    n = int(input("How many elements you want in the sequence? "))
#printing the 'n' elements of the Fibonacci Series

    x = []
    for i in range(n):
        if len(x) < 2:    
            x.append(b[i])
            print(x[i])
        else:
            x.append(x[i-1] + x[i -2])
            print(x[i])
# Count the number of elements in the sequence that are <= z
    z = int(input("Enter the biggest number of your Series. "))

    count = 0
    for i in x:
        if i <= z:
            count += 1
        else:
            break 

    print(f"The number of elements in the sequence that are lower than or equal to the biggest number are {count}.")    

if __name__ == "__main__":
    main()
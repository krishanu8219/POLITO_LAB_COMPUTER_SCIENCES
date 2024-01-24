x = []
x_0 = int(input("Enter the value for x1: "))
x_1 = int(input("Enter the value for x2: "))

b = [x_0,x_1]

n = int(input("How many elements you want in the sequence? "))

for i in range(n):
    if len(x) < 2:    
        x.append(b[i])
        print(x[i])
    else:
        x.append(x[i-1] + x[i -2])
        print(x[i])

z = int(input("Enter the biggest number of your Series. "))

count = 0
for i in x:
    if i <= z:
        count += 1
    else:
        break 

print(f"The number of elements that are lower than or equal to the biggest number are {count}")    

n=int(input("Enter the value:"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print()

#pattern 2
n = int(input("Enter the number of rows: "))  
for i in range(n + 1, 0, -1):    
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print()

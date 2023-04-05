lower = 900
upper = 1000
print("Even numbers between", lower, "and", upper, "are:")
for num in range(900,1001):
    for i in range(2, num):
        if (num % 2) == 0:
            print(num)
            num=num+1
            
     

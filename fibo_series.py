n = int(input ("Enter the number of terms required"))
a=0  
b=1  
c=0  
if n<= 0:  
    print ("Please enter a positive integer, the given number is not valid")    
elif n==1:  
    print ("The Fibonacci sequence of the numbers up to",n, ": ")  
    print(n)  
else:  
    print ("The fibonacci sequence of the numbers is:")  
    while c<n:  
        print(a)  
        d=a+b
        a=b
        b=d
        c=c+1

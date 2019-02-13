a=int(input("Give a number:"))
z=int(a)
print("The factors are: ")
i=1
while(i<=a):
    k=0
    t=0
    if (a%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                k=k+1
            j=j+1
        if(i>1):
            while (z % i == 0):
                z = z / i
                t = t + 1
        if(k==2):
             print(i,"^",t)
    i=i+1


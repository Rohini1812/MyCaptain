#AIM
#To generate a fibonacci sequence

#SOURCE CODE
n=int(input("Enter a number"))
f=0
s=1
print("Fibonacci Sequence")
print(f,end=" ")
print(s,end=" ")
i=2
while i<n:
    t=f+s
    f=s
    s=t
    i=i+1
    print(t,end=" ")
    

#Result
#The above program was executed successfully and the results are verified.

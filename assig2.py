#1st one - fibonacci numbers
num = int(input("enter the number: "));

f0 = 0;
f1 = 1;
count =0;

if(num<0):
    print("enter a positive number")
elif(num==0):
    print("Fibonacci Series: ",f0);
elif(num==1):
    print("Fibonacci Series: ",f0,",",f1,end=" ");
else:
    print("Fibonacci Series: ")
    while count<num+1:
        print(f0,end=",");
        fn = f0 +f1;
        f0=f1;
        f1=fn;
        count +=1;
        




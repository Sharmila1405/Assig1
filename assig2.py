#1st one - fibonacci numbers

f0 = 0;
f1 = 1;
num = int(input("enter the number: "));
print(f0,",",f1,end=" ");
while f1<num-1:
    fn=f0+f1;
    f0=f1;
    f1=fn;
    print(",",fn,end=" ");



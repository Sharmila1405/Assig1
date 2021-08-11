

n = input("enter the elememts of list1 separated by comma: ");

list1 = n.split(",");
list_1=[];

for i in list1:
    if int(i)>0:
        list_1.append(i)
        
print(*list_1,sep=",");



n1 = input("enter the elements in list2 separated by comma: ");

list2 = n1.split(",");
list_2=[]

for i in list2:
    if int(i)>0:
        list_2.append(int(i));
        
print(list_2)


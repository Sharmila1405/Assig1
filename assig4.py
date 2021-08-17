def most_frequent(s):
    d = {};
    for key in s:
        if key not in d:
            d[key] = 1;
        else:
            d[key] = d.get(key)+1;
    return d

s = input("please enter a string") 
mydict = {}
mydict = most_frequent(s.casefold())


mydict_sorted = sorted(mydict, key=mydict.get, reverse=True)
for r in mydict_sorted:
    print(r,"=",mydict[r],end=" ")



    
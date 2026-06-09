import os
user = input(" enter the name of a new item ")
f=open("item.txt","a")
f.write(user)
f.close()
f = open('item.txt',"r")
for x in f :
    print(x)
f.close()    



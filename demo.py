def hello():
   my_list=["hello","hai","welcome"]
   my_list.append("end")
   print(my_list)
   my_list.remove("hello")
   print(my_list)
   if "hai" in my_list:
       print("yes")
   else:
       print('no')

hello()    
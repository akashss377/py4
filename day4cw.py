fruits=['apple','bannana','orange']
vegetables = ['potato','tomato','cucumber']
beverage = ['pepsi','7up','Redbull']
fruits.append("graphes")
print(fruits)
vegetables.insert(1,"onion")
print(vegetables)
beverage.pop()
print(beverage)
inventory=[fruits,vegetables,beverage]
print(fruits[:2])
print(vegetables[-1])
print(len(vegetables))
if "water" in beverage :
    print("yes , water in the list")
else :
    print("No ")
first_items = (fruits[0],vegetables[0],beverage[0])
print(first_items)    
    


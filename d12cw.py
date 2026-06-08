try :
    title=input("enter the Book name : ")
    if not all(ch.isalpha() or ch.isspace() for ch in title ):
        raise ValueError("this is invaild")
    year = input("enter the year")
    if not (year.isdigit() and len(year)==4 and (year.startswith("19")or year.startswith("20"))):
     raise  ValueError("the year is invalid")
except ValueError as error :
    print(error)
finally : 
    print("program completed")
    print(title)
    print(year)
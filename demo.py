# def hello():
#    my_list=["hello","hai","welcome"]
#    my_list.append("end")
#    print(my_list)
#    my_list.remove("hello")
#    print(my_list)
#    if "hai" in my_list:
#        print("yes")
#    else:
#        print('no')

# hello()    



# from math import pi

# class Shape:
#     def __init__(self, name):
#         self.name = name

#     def area(self):
#         pass

#     def fact(self):
#         return "I am a two-dimensional shape."

#     def __str__(self):
#         return self.name


# class Square(Shape):
#     def __init__(self, length):
#         super().__init__("Square")
#         self.length = length

#     def area(self):
#         return self.length**2

#     def fact(self):
#         return "Squares have each angle equal to 90 degrees."


# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Circle")
#         self.radius = radius

#     def area(self):
#         return pi*self.radius**2


# a = Square(4)
# b = Circle(7)
# print(b)
# print(b.fact())
# print(a.fact())
# print(b.area())







# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y


# p1 = Point(1, 2)
# p2 = Point(2, 3)
# print(p1+p2)




# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
        
#     def __str__(self):
#          return "({0},{1})".format(self.x, self.y)
     
#     def __lt__(self, other):
#          self_mag = (self.x ** 2) + (self.y ** 2)
#          other_mag = (other.x ** 2) + (other.y ** 2)
#          return self_mag < other_mag
 
 
# p1 = Point(1,1)
# p2 = Point(-2,-3)
# p3 = Point(1,-1)
# print(p1 < p2)
# print(p2 < p3)
# print(p1 < p3)







# class Base: 
#     def __init__(self): 
#         self.a = "Python is Awesome!"
#         self.__c = "Mashup Stack"
  
# Creating a derived class 
# class Derived(Base): 
#     def __init__(self): 
          
#         # Calling constructor of 
#         # Base class 
#         Base.__init__(self)  
#         print("Calling private member of base class: ") 
#         print(self.__c) 
# Driver code 
# obj1 = Base() 
# print(obj1.a) 

# raises an AttributeError  
# print(obj1.__c)

# raises an AttributeError 
# obj2 = Derived()



# class Mycourse:
#     def __init__(self  ,course,fees):
#         self.course = course
#         self.fees = fees
#     def final (self):
#         print(f"my {self.course} price is  {self.fees}")    
# obj=Mycourse("python",400)
# obj1=Mycourse("javascript",300)
# obj.fees = 200
# del obj1.fees
# obj.final()
# obj1.final()      
        
class market:
    def __init__(self,vegitables,fruits):
        self.vegitables = vegitables
        self.fruits = fruits
    def out(self):
        print(f"{self.vegitables},{self.fruits}")
class final(market):
    def __init__(self, vegitables, fruits):
        market.__init__(vegitables, fruits)
    
  
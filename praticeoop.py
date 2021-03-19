# class person:
#     def __init__(self):
#         print("hello nepal")
#     def func(self):
#         print("Hello my name is" +self.name)
# obj = person("ram")
# obj.name

#
# class Introduction:
#     x = 12
# p1 = Introduction()
# print(p1.x)


# class simpleinterest:
#    def take_value(s):
#     p = int(input("enter principal"))
#     t = int(input("enter time"))
#     r = int(input("enter rate"))
#     return p,t,r
#
#    def calculate_value(self,p,t,r):
#
#       return p*t*r/100
#
#    # def display_value(self):
#    #  return self.calculate_value(self)
#
# obj = simpleinterest()
# obj.take_value()
# obj.calculate_value()
# # obj.display_value()
#
#
#

# class complex:
#     def fun(self,real,imag):
#         self.r = real
#         self.i = imag
#         return real,imag
# x = complex()
# print(x.fun(3,2))
#a = ["mary","sita","gita","ram"]
# for i in range(5):
#     print(i)

# def fib(n):
#     a,b = 0,1
#     result = []
#     while a<n:
#         result.append(a)
#         a,b = a ,a+b
#     return result
#
# fib(200)

# class Fruits:
#     def __init__(self):
#         return "i am fruits"
#
#     def get_fruits(self):
#         return"got fruoits"
#
# class Mango(Fruits):
#     super().__init__()
#
# obj=Mango()
# obj.get_fruits()
#

# mylist= {"name":"ashish","roll":4}
#
# print(type(mylist))
#

#.mro()
#bound method
#datetime module
#
# words = ["python","ram","sita"]
# for word in words:
#  print(len(word))

# class Example:
#     __name = "ashish"
#
#
#     @property
#     def get_name(self):
#         return self.__name
#     @get_name.setter
#     def get_name(self,n):
#         self.__name = n
#
#
#
# obj = Example()
# obj.get_name="hari"
# print(obj.get_name)



# class Friend:
#     def __init__(self):
#         self.job = "None"
#
#     def getJob(self):
#         return self.job
#
#     def setJob(self, job):
#         self.job = job
#
# Alice = Friend()
# Bob = Friend()
#
# Alice.setJob("Carpenter")
# Bob.setJob("Builder")
#
# print(Bob.job)
# print(Alice.job)











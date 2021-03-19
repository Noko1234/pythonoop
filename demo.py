# def names(*name,**age):
#     print(name)
#     print(age)
#
# names('ram','shyam', name='Ram',age=20)
#
# x = 10
# def test():
#     global x
#     print(x)
#     x = x + 4
#     print(x)
# test()

# fucntion returns value
#
# def test():
#     def get():
#         return "hello get"
#
#     return get
#
# print(test()())


# def get_name():
#     num = int(input("enter the number of students:"))
#     students=[]
#     x = 0
#     while x < num:
#       name = input("enter the name os students")
#       students.append(name)
#       x += 1
#     return students
#
# def display():
#  for name in get_name():
#      print(name)
#
#
# display()
#

# global total
# def add():
#      name = input("enter the name")
#      mark1 =int(input("enter the marks"))
#      mark2 =int(input("enter the marks"))
#      mark3 =int(input("enter the marks"))
#      mark4 =int(input("enter the marks"))
#      total= mark1 + mark2 +mark3 +mark4
#      avg = total/4
#      return total
#
# def avg():
#
#     return total/4
# def display():
#
#     print(add())
#     print(avg())
#
# display()

# def calc_tax(sales_total, tax_rate):
#   tax = sales_total * tax_rate
#   return


# def total_number(*number):
#  size_of_array = len(number)
#  x = 0
#  sum = 0
#  while x< size_of_array:
#      sum += number[x]
#      x += 1
#  print(sum)
# total_number(1,2,3,4,5,6)


# def total_number(*number):
#     size_of_array = len(number)
#     i = 0
#     even_total = 0
#     odd_total = 0
#     while i < size_of_array:
#         if number[i] % 2 == 0:
#             even_total += number[i]
#         else:
#             odd_total += number[i]
#
#         i += 1
#
#     print(f"Total even number:{even_total}")
#     print(f"Total odd number:{odd_total}")
#
#
# total_number(1, 2, 3, 4, 5, 6)



# def number(*num):
#  size_of_array=len(num)
#  i = 0
#  even = 0
#  odd = 0
#  while i < size_of_array:
#      if num % 2==0:
#       even+= num[i]
#      else:
#       odd+= num[i]
#       i+=1
# print(f"total even is {even}")
# print(f"total odd number is {odd}")
# number(2,3,4,5,6)

# for x in range(6):
#     for y in range(5):
#      print(f"({x},{y})")


#decorator check
# zero check
# check>100



# def zerocheck(anyFunction):
#     def innerfunc(x,y):
#
#       if y==0:
#         print("y is zero ")
#       return x + y
#
#     return innerfunc
#
# def total_check(anyfunction):
#     def innerfunc(check):
#         if check>100:
#             print("enter less than 100")
#         return check
#     return innerfunc()
#
# @total_check
# @zerocheck
#
# def add(x,y):
#  if y==0:
#      print("enter any number")
#  return x + y
#
#
#  print(add(2,0))






# def make_pretty(anyfunction):
#     def inner()
#         print("I got decorated")
#
#     return inner()
#
# @make_pretty
# def ordinary():
#  return "Hello"

# def insert():
#  return "demo inserted"
#
#  def update():
#   return "demo updated"
#
# handle = open('record.txt','w')
# handle.write("hello python")
# handle.close()


# a = int(input("enter anynumber"))
# b = int(input("enter number "))
# sum = a + b
# handle = open('record.txt','w')
#
# handle.write(f"{sum}")
#
#

# def insert():
#
#
#
# def show():
# print(insert ko item print garne)
# def update()
# def delete



#obj = open('record.txt','r')
# print(obj.read())
# print(obj.readlines())



 
#import csv

# with open('aaaa.csv','r') as file:
#  get_data = csv.DictReader(file)
#  for user in get_data:
#      print(user)

#
# import csv
#
# with open('data.csv','w',newline='') as files:
#    header = ['sn','name','age','address']
#    fs = csv.DictWriter(files, fieldnames=header)
#    fs.writeheader()
#    fs.writerow({'sn': 1,'name': 'ram','address': 'kathmandu'})
#
#
#
# fh = open("database.txt","r")
# print(fh.read())
# fh.close()
# import csv
# with open ('data.csv','r') as file:
#    get_data = csv.DictReader(file)
#    for user in get_data:
#       print(user)
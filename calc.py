print(" Welcome to my calc! ")
print("1 = +")
print("2 = -")
print("3 = *")
print("4 = %")
opt1=int(input("Please Enter your first number: "))
opt2=int(input(" Pleate choose your operator: "))
opt3=int(input(" please enter your second number: "))
print()
if opt2 == 1:
     result = opt1 + opt3
     print (result)
if opt2 == 2:
     result = opt1 - opt3
     print (result)
if opt2 == 3:
     result = opt1 * opt3
     print (result)
if opt2 == 4:
     if opt3 == 0:
          print(" you can't devide by zero! ")
     else:
          result = opt1 % opt3
          print (result)
else:
     print(" Error! ")


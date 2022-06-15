'''
    the condtions
    if codtion ture:
    run the code
    else flase:
    run another code 

'''
'''
'uesr name and password: '
name = "Ahmed"
password = "google"
'ask the user for his name'
log = input("type ur name: ")
if log == name:
    print("weclome " + name)
'ask the user for password'
logPass = input("type ur password: ")
if logPass == password:
    print("weclome")
'''
'nasted if'
'''
Sum = 200
guess = 200
if guess == Sum:
    print("you have one point: ")
    if guess > 150:
        print("the number is bigger than 150")
    if guess < Sum:
        print("worng the  sum number is bigger: ")
else:
    print("u have to type i number")
'''
'and % or '
''''
name = "ahcmed"
password = "25250"
if name == "ahmed" and password == "25250":
    print("welcome ahmed: ")
else:
    print("password or username is worng try agin!")
Myname = "ahmed"
Hisname = "acli"
if Myname == "ahmed" or Hisname == "ali":
    print("hey")
x = 50
y = 70
z = 45
if all([x == 50, y == 70, z ==45]):
    print("done")
'''
'single if'
x = 100
print("done") if x == 100 else print("worng")

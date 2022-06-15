def avrage(x,y,z):
    resualt = x+y+z/3
    return resualt
print("type i three numbers for get the avragge...")
x = int(input("type the frist number: "))
y = int(input("type the secend number: "))
z = int(input("type the theerd number: "))
print(f"the first num is {x} the secend number is {y} the threed number is {z}")
total = x+y+z
print(f"the total of ur number is {total}")
av = avrage(x,y,z)
print (f"the avrrage is {av}")


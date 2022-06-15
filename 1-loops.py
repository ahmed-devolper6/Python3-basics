m = int(input("type i number for get squre: "))
print("number|\t|sqaure")
print("<_______________>")
for m in range(m, 11):
    print(f"{m}\t{m*m}")
print("<_______>")

start = int(input("Enter the start: "))
end = int(input("Enter the end: "))

for m in range(start,end+1):
    for x in range(1,10):
        print(f"{m} X {x} = {x*m}")
    print("_______")

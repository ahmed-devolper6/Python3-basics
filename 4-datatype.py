'''
int
float
bool
str
list
tuple
dict
'''
print("\t String")
print("<________________>")
d = "ahmed"
print(d.lower())
print(d.upper())
print(d.isupper())
print(d.islower())
Title = "my name is ahmed im i django devloper"
print(Title.title())
mypath = "c/value/pic/ahmed/spi/img.png"
mypath.split()
print(mypath.split('/'))
print(mypath.split('/')[-1])
replaceName = "my name is ahmed"
print(replaceName)
c = input("type ur name: ")
print(replaceName.replace("ahmed", c))


print("\t Tuple")
print("<__________________________>")
a = int(input("enter i number: "))
b = int(input("enter i number: "))
w = int(input("enter i number: "))
z = int(input("enter i number: "))
tuples = (a , b , w , z)
print(f"all ur number is{tuples}")
mins = min(tuples)
print(f"the min of ur tuple is {mins}")
Max = max(tuples)
print(f"the max number is {Max}")
Length = len(tuples)
print(f"the Length of ur tuple is: {Length}")


print("\t List")
print("<__________________________>")
List = [45,787,454,54,600]
print(List)
List.append(int(input("add i number on the last of list: ")))
print(List)
List.insert(int(input("where u want to add ur number: "))
            ,int(input("insert i number to the list: ")))
print(List)
List.remove(int(input("what number u want to remove: ")))

print("the sort is: ")
List.sort()
print(List)
print("the revrse sort is: ")
List.reverse()
print(List)

print("\t dict")
print("<__________________________>")
aa = input("type i key for value 50: ")
ss = input("type i key for value 40: ")
ff = input("type i key for value 80: ")
Dict = {aa:50, ss:40 , ff:80}
print(Dict)
print("add i key and value for dict")
Dict[input("the key: ")] = int(input("type i value of ur key: "))
print(f"the keys is {Dict.keys()}")
print(f"the vales is {Dict.values()}")
print(f"the itms is {Dict.items()}")

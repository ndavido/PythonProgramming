#! usr/bin/python3

class MyFirstClass:
    pass
object1 = MyFirstClass()
object2 = MyFirstClass()
object3 = MyFirstClass()
object4 = MyFirstClass()

print(object1)
print(object2)
print(object3)
print(object4)

print("----- Second Class -----")

class MySecondClass():
    x = 2
    
object21 = MySecondClass()
object22 = MySecondClass()
object23 = MySecondClass()

print(object23)
print(object21)
print(object22)

print(object21.x)

object21.x = 3
print(object21.x) 
print(object22.x) 
print(object23.x)

del object21
# print(object21.x) NameError: name 'object21' is not defined.


#Python has three sequence datatypes:
'''
    string 
    list
    tuple

'''

print("All sequences are ordered, indexed int, and have length")

print("slice reassignment")

a = [0,1,4,5,6,7,8]
print(a)

a[2:4] = [10,11,12,13,14]

print(f"\n{a}") 
print("This means that the slicing index is for the elements to be removed!")

a[2:2] = [2,3]
print(a)
print("That means to insert elements without removing the existing ones use [i:i] \n\n Which makes sense now coz we command to remove the element from i to i-1 position , which here is i! that is i itself!!. so no element is removed !!!!AGHHH knowing that brings peace V")


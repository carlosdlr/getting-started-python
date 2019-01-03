a = [1,2,3]
b = a 

#this will print true because both variables are pointing to the same object
print(a is b)

#this will print true because both variables have the same values in this case 1,2,3
print(a == b)

c = list(a)

#this will print true because both variables have the same values in this case 1,2,3
print(a == c)

#this will print false becuase these variables are pointing to different objects in this case c is pointing to a new list base on the a values
print(a is c)


# "is" expressions evaluate to True if two 
# variables point to the same object

# "==" evaluates to True if the objects 
# referred to by the variables are equal

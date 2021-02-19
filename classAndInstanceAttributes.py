#class attributes
#Class attributes belong to the class itself they will be shared by all the instances.

class sampleclass: 
    count = 0
  
    def increase(self): 
        sampleclass.count += 1
  
s1 = sampleclass() 
s1.increase()         
print(s1.count) 
s2 = sampleclass() 
s2.increase() 
print(s2.count) 
  
print(sampleclass.count)

"""
OUTPUT:
1              
2                           
2

"""




#Instance attributes
#Unlike class attributes, instance attributes are not shared by objects. 
#Every object has its own copy of the instance attribute

# To list the attributes of an instance/object, we have two functions:-
# 1. vars()– This function displays the attribute of an instance in the form of an dictionary.
# 2. dir()– This function displays more 
#   attributes than vars function,as it is not limited to instance. 
#   It displays the class attributes as well. 
#   It also displays the attributes of its ancestor classes.

class emp: 
    def __init__(self): 
        self.name = 'xyz'
        self.salary = 4000
  
    def show(self): 
        print(self.name) 
        print(self.salary) 
  
e1 = emp() 
print("Dictionary form :", vars(e1)) 
print(dir(e1))


"""
OUTPUT:
Dictionary form :{'salary': 4000, 'name': 'xyz'}
['__doc__', '__init__', '__module__', 'name', 'salary', 'show']


"""
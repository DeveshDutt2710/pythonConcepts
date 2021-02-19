#default arguments in python

def student(firstname, lastname ='Mark', standard ='Fifth'):
     print(firstname, lastname, 'studies in', standard, 'Standard')
 
# 1 positional argument
student('John') 
 
# 3 positional arguments                         
student('John', 'Gates', 'Seventh')     
 
# 2 positional arguments  
student('John', 'Gates')                  
student('John', 'Seventh')


#link : https://www.geeksforgeeks.org/default-arguments-in-python/
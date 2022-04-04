''' a variable name can contain alphabet ,digits and variable , a variable name can only start with an alphabet and underscore ,if variable 1a = 11 then it is invalid sentence coz name can not start with num it can be a1_anything , no while space is allowed to be used inside a variable name , variable names are case sensitive (example-line 26-29) '''
'''dat types 
primary :- integer, float , string , booleans,none
'''
a = 11 #integer  
b = 0.11 # float
c = "sha" # string "" and also '' single code and also it '''can also be written in triple code too coz it is assigned'''
d = True # true and false are boolean 
e = None # if d = none then it prints none instead true 
#print variables 
print(a)
print(b)
print(c)
print(d)
print(e)
# printing the type of variables
print(type(a)) 
print(type(b))
print(type(c))
print(type(d))
print(type(e))
# python can automatically identifies the type of data 

#keywords can not be used in making variable  coz  it is not recomende it might break  the programme.

s = 1
S = 123
print(s)
print(S)

f = '3'
print(type(f)) # it prints str coz of ''
g = input("enter any num:  ")
print(g)
print(type(g)) #it prints str as enter...... is written in ""
g =int(g) # we need to convert 
print(g)
print(type(g)) 
#python .\variable.py
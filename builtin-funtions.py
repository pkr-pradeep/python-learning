#print
str = 'Hi I am there'
if 'hi' in str:
 print(1)
else:
 print(2)

print("absolute value of -1:",abs(-1))
print("if all have the value then true, else false\n It can be list, tuple or any other iterable")
list1=[1,2,'']
print("all(",list1,") is:",all(list1))
print("any() is opposite or all()")
print("any(",list1,") is:",any(list1))

#0b prefix means binary i.e. 0b111
print("binary of integer 7 is:",bin(7)) 
#,"\nbinary of float 7.0 is", bin(7.0) # will throw an error as it is float
#like that for octadecimal prefix will be 0o12
print("octadecimal of 10 is:",oct(10)) 

print("boolean of 1 is:",bool(1))
#True
print("boolean of 0 is:",bool(0))
False
print("boolean of 0.1 is:",bool(0.1))
#True
print("boolean of '' is:",bool(''))
False
print("boolean of 't' is:",bool('t'))
#True
print("boolean of 'false' is:",bool('false'))
#True
#print("boolean of false is:",bool(false))#Error: name 'false' is not defined
print("boolean of False is:",bool(False))
False
print("boolean of True is:",bool(True))
#True

#callable
def method() :
 return 1

obj = method
value = method()
print(obj," contains value ",value)

print("method is callable:",callable(method))
print("(built-in method)list method is callable:",callable(list))
print("a variable is not, like callable([1,2]) is ", callable([1,2]), ' or callable(True) is:', callable(True))


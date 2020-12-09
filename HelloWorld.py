import math

print("2+3=",2+3)
x = int(input("write an integer,x="))
if x < 5:
 print("x is less than 5")
elif x > 5:
 print("x is greater than 5")
else:
 print("x equals to 5")

def helloworld():
 print("hello world")

def addNumbers(num1, num2):
 sum = num1+num2
 return sum

helloworld()
b,c=5,6
d = addNumbers(b,c) # calling parameterized function
print("numbers are:",b,c); print("\n summation of these two nums is: ",d) #here semicolon is not end, its continuation of next line on the same line

summ = lambda x,y:x+y #lambda expression
print("summation of 6 and 7: ",summ(6,7))
hundred = math.pow(10,2)
print("10 power of 2:",hundred)
y = float(input("write a decimal number,y="))
print("ceiling:",math.ceil(y))
print("flooring:",math.floor(y))
print("absolute value:", math.fabs(y))
print("log of 10 base 2:",math.log(10,2))
str = "hELLo wOrld"
print("(sentence casing)capitalize hELLo wOrld:", str.capitalize())
print("how many o in the above string? ",str.capitalize().count("o"))
str = 'i am a good guy'
#print("index of g in 'i am a good guy'",str.find('g'))
print("index of g in"+" "+str+" is:", str.find('g'))

multiLineStr = """hi there,
how are you
are you good
I am fine"""
print(multiLineStr)

#join to concat
str1 = "_" #this is the separator of each word
str2=("i","am",'a','developer')
str3 = str1.join(str2)
print(str3)

#Lists
list1 = [1,2,3,4,5]
list2 = [1, "hey", 2, 'hey! nice to see you',3, 'hey buddy',1,'hey! when did you come home?']
print("list1:",list1,"\n list2:", list2,
"\n list2[1]:",  list2[1], 
"\n list2 from index 2 to 5:", list2[2:5])

#can access all the element by two ways
#print(list1)
print(list1[:])

#begin from index zero to some index
print(list1[:4])
#from some index to end index
print(list1[3:])

list1.append(5)
print("after appending a value to end, list is:",list1)
list1[5] = 6
print("it was a mistake, added 5, now updating it with 6. list is:",list1)

#del statement is used to remove the element in the list, here the index of the list needed
del list1[5]
print("6th value is not needed, deleted, now the list is:", list1)

#in remove() we  need to specify the element itself to delete and it deletes the first occurence
list1.append(5)
list1.remove(5)
print(list1)

#Tuple
#Like list, tuple is used to store multiple value which may or may not be of same type, values are separated by commas and enclosed by paranthesis
tuple1 = (1,2,3,4)
tuple2 = (1,"hi",2,"hello")
print(tuple2)

#accessing elements are same in tuple like tuple1[2:] tuple[:3]
print(tuple1[2])
print(tuple1[:])
print(tuple1[2:])
print(tuple1[:3])
#as tuples are immuatble, we cant perform update or deletion on it
#but we can delete whole tuple using del statement
del tuple2
#print(tuple2) #name 'tuple2' is not defined error will come
#tuples to use when you know the elements we get are fixed in size

#dictionary
dict1 = {"name":"Pradeep","age":28,"occupation":"Software developer"}
print(dict1)
print(dict1['age'])
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#adding new elements
dict1['address']='Odisha'
print(dict1)
#update the element
dict1['name']='Pradeep Rout'
print(dict1)

thisdict['owner']="pkr"
print(thisdict)

#deleing an element
del thisdict['owner']
print(thisdict)

#del thisdict 
#this is used to remove entire dictionary

#rather than deleting entire dictionary
#we can clear all its elements and make it empty
thisdict.clear()
print(thisdict)
#Example of explicit type conversion in Python from int to string, bollean, None, and float.
x= 10
x1 = str(x)  #Explicit type conversion from integer to string
x2 = bool(x)  #Explicit type conversion from integer to boolean
x3 = float(x)  #Explicit type conversion from integer to float  
#Note: In Python, any non-zero integer is considered True when converted to boolean, and 0 is considered False.

print(type(x),type(x1),type(x2),type(x3))  #Prints the types of the converted variables
print(x1, x2, x3)  #Prints the converted values



#Example of explicit type conversion in Python from bolean to string, integer,  None, and float.
word=False       #Always false and true write first letter as capital letter............
word1 = str(word)  #Explicit type conversion from boolean to string
word2 = int(word) #Explicit type conversion from boolean to integer
word3 = float(word)  #Explicit type conversion from boolean to float

print(type(word),type(word1),type(word2),type(word3))  #Prints the types of the converted variables
print(word1, word2, word3,)  #Prints the converted values


#Example of explicit type conversion in Python from string to integer, boolean, float.
string = "Abinash Kar "  #String representation of an integer
string1 = int(len(string))  #Explicit type conversion from string to integer (length of the string)
string2 = bool(string)  #Explicit type conversion from string to boolean (non-empty string is True)
string3 = float(len(string))  #Explicit type conversion from string to float (length of the string)

string4 = '123'  #String representation of an integer
string5 = int(string4)  #Explicit type conversion from string to integer (valid integer string)
string6 = float(string4)  #Explicit type conversion from string to float (valid integer string)
string7 = bool(string4)  #Explicit type conversion from string to boolean (non-empty string is True)

'''Note: The string must be convertible to an integer, otherwise it will raise a ValueError.
In this case, we are converting the length of the string to an integer and float.  
If you want to convert the string directly to an integer, it must represent a valid integer value.
For example, if the string was "123", then int(string) would work, but "Abinash Kar" would not.'''

print(type(string),type(string1),type(string2),type(string3),type(string5),type(string6),type(string7))  #Prints the types of the converted variables
print(string1, string2, string3, string5, string6, string7)  #Prints the converted values

#Example of explicit type conversion in Python from None to integer, boolean, float.
none_value = None  #None value
none1 = int(bool(none_value))  #Explicit type conversion from None to integer (0)
none2 = bool(none_value)  #Explicit type conversion from None to boolean (False)
none3 = float(bool(none_value))  #Explicit type conversion from None to float (0.0) 

'''Note: Converting None to an integer or float will raise a TypeError,
so we first convert None to boolean, which is False, and then convert that to int 
and float, resulting in 0 and 0.0 respectively'''

print(type(none_value), type(none1), type(none2), type(none3))  #Prints the types of the converted variables
print(none1, none2, none3)  #Prints the converted values

#Example of explicit type conversion in Python from float to integer, boolean, None, and string.
float_value = 3.14  #Float value
float1 = int(float_value)  #Explicit type conversion from float to integer (truncates the decimal part)
float2 = bool(float_value)  #Explicit type conversion from float to boolean (non-zero float is True)
float3 = str(float_value)  #Explicit type conversion from float to string 

print(type(float_value), type(float1), type(float2), type(float3))  #Prints the types of the converted variables
print(float1, float2, float3)  #Prints the converted values..


''' Note: There is no direct way to convert an integer to None and othr data structure like [dictionary,set,tuple,list] in Python. 
# None is a unique object representing the absence of a value.
# However, you can assign None to a variable that previously held an integer value. 
# This is not a type conversion but rather a reassignment.'''

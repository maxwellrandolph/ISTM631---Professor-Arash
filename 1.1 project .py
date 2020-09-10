Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> "Greetings!"
'Greetings!'
>>> name=input("Maxwell Crawford Randolph")
Maxwell Crawford Randolph
>>> print(name)

>>> name("Maxwell Crawford Randolph:")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    name("Maxwell Crawford Randolph:")
TypeError: 'str' object is not callable
>>> name=input("Maxwell Crawford Randolph:")
Maxwell Crawford Randolph:
>>> name=input("Enter your name:")
Enter your name:Maxwell Crawford Randolph
>>> name
'Maxwell Crawford Randolph'
>>> print(name)
Maxwell Crawford Randolph
>>> name
'Maxwell Crawford Randolph'
>>> first = int(input('Enter the first number: '))
Enter the first number: 12
>>> second = int(input('Enter the second number: '))
Enter the second number: 34
>>> second = int(input('Enter the second number: '))
Enter the second number: 45
>>> print("the sum is ", first+second)
the sum is  57
>>> radius = int(input('Enter the radius: '))
Enter the radius: 2
>>> print("the area of a circle is ", 3.14 * radius ** 2)
the area of a circle is  12.56
>>> input(Maxwell)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    input(Maxwell)
NameError: name 'Maxwell' is not defined
>>> input(int(maxwell)
      name = input(int(maxwell))
      
SyntaxError: invalid syntax
>>> name=input(int(maxwell)

>>>name=input(int(Enter your first name: )
	      
SyntaxError: invalid syntax
>>> name=input(int(Enter your first name: )
	   
SyntaxError: invalid syntax
>>> name=input(int('Enter your first name: '))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    name=input(int('Enter your first name: '))
ValueError: invalid literal for int() with base 10: 'Enter your first name: '
>>> name = int(input('Enter your first name: '))
Enter your first name: Maxwell
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    name = int(input('Enter your first name: '))
ValueError: invalid literal for int() with base 10: 'Maxwell'
>>> 2
2
>>> name = input('Enter your first name: ')
Enter your first name: Maxwell
>>> print
<built-in function print>
>>> print(name)
Maxwell
>>> 
>>> radius = float(int(input('Enter the radius: ')))
Enter the radius: 2
>>> print('The area of the circle is ', 3.14 * radius ** 2)
The area of the circle is  12.56
>>> >>> radius = float(int(input('Enter the radius: ')))
SyntaxError: invalid syntax
>>> radius = float(int(input('Enter the radius: ')))
Enter the radius: 2.1
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    radius = float(int(input('Enter the radius: ')))
ValueError: invalid literal for int() with base 10: '2.1'
>>> radius = int(float(input('Enter the radius: ')))
Enter the radius: 2.1
>>> print(The area of a circle is ', radius * 3.14 **2)
      
SyntaxError: invalid syntax
>>> print('The area of a circle is ', radius * 3.14 ** 2)
The area of a circle is  19.7192
>>> 
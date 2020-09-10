Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> length = float(input("enter length; "))
enter length; 
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    length = float(input("enter length; "))
ValueError: could not convert string to float: ''
>>> 
>>> length = float(input("enter length "))

area = length*length

print(The area of the square is ", area, "square units")

SyntaxError: multiple statements found while compiling a single statement
>>> =RESTART
SyntaxError: invalid syntax
>>> length = float(input("enter length "))

enter length 45
>>> area = length*length

print(The area of the square is ", area, "square units")
      
SyntaxError: multiple statements found while compiling a single statement
>>> length = float(input("enter length "))

area = length*length
SyntaxError: multiple statements found while compiling a single statement
>>> area = length*length
>>> print(The area of the square is ", area, "square units")
      
SyntaxError: invalid syntax
>>> print("the area is ", area, "square units")
the area is  2025.0 square units
>>> 
========== RESTART: /Users/skywalker/Desktop/test area of square 3.py ==========
Enter the length: 
========== RESTART: /Users/skywalker/Desktop/test area of square 3.py ==========
Enter the length: 88
The area is  7744.0 square units
>>> 
========== RESTART: /Users/skywalker/Desktop/test area of square 3.py ==========
Enter the length: -57
The area is  3249.0 square units
>>> 
========== RESTART: /Users/skywalker/Desktop/test area of square 3.py ==========
Enterthe gross income: 
========== RESTART: /Users/skywalker/Desktop/test area of square 3.py ==========
Enter the gross income: 10000
>>> numDependents = int(input("Enter the number of dependents: "))
Enter the number of dependents: 1
>>> 
========== RESTART: /Users/skywalker/Desktop/test area of square 3.py ==========
Enter the gross income: 10000
Enter the number of dependents: 1
The income tax is $-600.0
>>> 
========== RESTART: /Users/skywalker/Desktop/test area of square 3.py ==========
Enter the gross income: 40000
Enter the number of dependents: 1
The income tax is $5400.0
>>> TAX_RATE = .20

STANDARD_DEDUCTION = 10000.0

DEPENDENT_DEDUCTION = 3000.0

grossIncome = float(input("Enter the gross income: "))

numDependents = int(input("Enter the number of dependents: "))

taxableIncome = grossIncome - STANDARD_DEDUCTION - (DEPENDENT_DEDUCTION * numDependents)

incomeTax = taxableIncome * TAX_RATE

print("The income tax is $" + str(incomeTax))

SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> emptyv''
SyntaxError: invalid syntax
>>> emptyv = ''
>>> empty
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    empty
NameError: name 'empty' is not defined
>>> emptyv
''
>>> print"emptyv"
SyntaxError: invalid syntax
>>> print('emptyv')
emptyv
>>> 
===== RESTART: /Users/skywalker/Desktop/2.3 strings,assignment,comments.py =====
>>> 
===== RESTART: /Users/skywalker/Desktop/2.3 strings,assignment,comments.py =====
>>> 
===== RESTART: /Users/skywalker/Desktop/2.3 strings,assignment,comments.py =====
empty
>>> 
===== RESTART: /Users/skywalker/Desktop/2.3 strings,assignment,comments.py =====
empty
Traceback (most recent call last):
  File "/Users/skywalker/Desktop/2.3 strings,assignment,comments.py", line 4, in <module>
    empty
NameError: name 'empty' is not defined
>>> 
===== RESTART: /Users/skywalker/Desktop/2.3 strings,assignment,comments.py =====
emptyv
Traceback (most recent call last):
  File "/Users/skywalker/Desktop/2.3 strings,assignment,comments.py", line 4, in <module>
    empty
NameError: name 'empty' is not defined
>>> 
===== RESTART: /Users/skywalker/Desktop/2.3 strings,assignment,comments.py =====
emptyv
this is a sentence
so i will do two lines
.
.
.
.
>>> 
===== RESTART: /Users/skywalker/Desktop/2.3 strings,assignment,comments.py =====
emptyv
this is a long sentence
so i will do many lines
.
.
.
.
this sentence is a long one
very long/n./n./n
>>> 
===== RESTART: /Users/skywalker/Desktop/2.3 strings,assignment,comments.py =====
emptyv
this is a long sentence
so i will do many lines
.
.
.
.
this sentence is a long one
very long
.
.

>>> 
===== RESTART: /Users/skywalker/Desktop/2.3 strings,assignment,comments.py =====
emptyv
this is a long sentence
so i will do many lines
.
.
.
.
this sentence is a long one
very long
.
.

yo extendo








Doneski
>>> 'hi '+'there '+' Sophie'
'hi there  Sophie'
>>> 
===== RESTART: /Users/skywalker/Desktop/2.3 strings,assignment,comments.py =====
emptyv
this is a long sentence
so i will do many lines
.
.
.
.
this sentence is a long one
very long
.
.

yo extendo



Doneski
>>> 
===== RESTART: /Users/skywalker/Desktop/2.3 strings,assignment,comments.py =====
emptyv
this is a long sentence
so i will do many lines
.
.
.
.
this sentence is a long one
very long
.
.

yo extendo



Doneski
testtesttesttesttesttesttesttesttesttest
>>> 
===== RESTART: /Users/skywalker/Desktop/2.3 strings,assignment,comments.py =====
emptyv
this is a long sentence
so i will do many lines
.
.
.
.
this sentence is a long one
very long
.
.

yo extendo



Doneski
test test test test test test test test test test 
>>> 
===== RESTART: /Users/skywalker/Desktop/2.3 strings,assignment,comments.py =====
emptyv
this is a long sentence
so i will do many lines
.
.
.
.
this sentence is a long one
very long
.
.

yo extendo



Doneski
test test test test test test test test test test 
>>> 
===== RESTART: /Users/skywalker/Desktop/2.3 strings,assignment,comments.py =====
emptyv
this is a long sentence
so i will do many lines
.
.
.
.
this sentence is a long one
very long
.
.

yo extendo



Doneski
test test test test test test test test test test 
Traceback (most recent call last):
  File "/Users/skywalker/Desktop/2.3 strings,assignment,comments.py", line 33, in <module>
    x = DOG
NameError: name 'DOG' is not defined
>>> dog = x
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dog = x
NameError: name 'x' is not defined
>>> input(string("x = ")
      x
      
SyntaxError: invalid syntax
>>> x = input(string("let x be "))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    x = input(string("let x be "))
NameError: name 'string' is not defined
>>> x = string(input("let x be "))
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    x = string(input("let x be "))
NameError: name 'string' is not defined
>>> str
<class 'str'>
>>> str
<class 'str'>
>>> x = str(input("let x be "))
let x be dog
>>> y = str(input("let y be "))
let y be cat
>>> x+y
'dogcat'
>>> "the "+x+" chases the "+y
'the dog chases the cat'
>>> x * 4
'dogdogdogdog'
>>> 'x '*4
'x x x x '
>>> x+' '*4
'dog    '
>>> (x )*4
'dogdogdogdog'
>>> string(Maxwell\nRandolph)
SyntaxError: unexpected character after line continuation character
>>> print("Maxwell\nRandolph")
Maxwell
Randolph
>>> print('''Maxwell
Randolph''')
Maxwell
Randolph
>>> print('Maxwell /nRandolph)
      
SyntaxError: EOL while scanning string literal
>>> print('Maxwell \nRandolph')
Maxwell 
Randolph
>>> print('''Maxwell
Randolph''')
Maxwell
Randolph
>>> print('''Maxwell

Randolph''')
Maxwell

Randolph
>>> print('Maxwell\n\n Randolph
      
SyntaxError: EOL while scanning string literal
>>> print('Maxwell\n\n Randolph')
Maxwell

 Randolph
>>> print('''Maxwell


Randolph''')
Maxwell


Randolph
>>> print('''Maxwell

 Randolph''')
Maxwell

 Randolph
>>> chr(97)
'a'
>>> chr(69)
'E'
>>> #2.4 Num
>>> #2.4 Numerical Data Types and Character Sets
>>> """ASCII Codes"

ord(a)
ord('a')
"""
'ASCII Codes"\n\nord(a)\nord(\'a\')\n'
>>> ord(a)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    ord(a)
NameError: name 'a' is not defined
>>> ord('a')
97
>>> ord('A')
65
>>> chr(103)
'g'
>>> chr(100000004)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    chr(100000004)
ValueError: chr() arg not in range(0x110000)
>>> chr(1004)
'Ϭ'
>>> chcode = int(ord(inputs('enter a character: ')))
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    chcode = int(ord(inputs('enter a character: ')))
NameError: name 'inputs' is not defined
>>> chcode = int(ord(input('enter a character: ')))
enter a character: 0
>>> chcode = int(ord(input('enter a character: ')))
enter a character: O
>>> chcode
79
>>> chcode
79
>>> chcode = int(ord(input('enter a character: ')))
enter a character: R
>>> chcode
82
>>> print(chcode)
82
>>> 
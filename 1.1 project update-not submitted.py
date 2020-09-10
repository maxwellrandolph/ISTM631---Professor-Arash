Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> input(Maxwell)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    input(Maxwell)
NameError: name 'Maxwell' is not defined
>>> input()
Maxwell
'Maxwell'
>>> input('Enter your first name: ')
Enter your first name: Maxwell
'Maxwell'
>>> print("Greetingss, " + Name)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print("Greetingss, " + Name)
NameError: name 'Name' is not defined
>>> print('Greetings, " + Enter your first name: )
      
SyntaxError: EOL while scanning string literal
>>> FirstName = input ('Enter your first name: ')
Enter your first name: Maxwell
>>> Print ('Greetings, ' + FirstName)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    Print ('Greetings, ' + FirstName)
NameError: name 'Print' is not defined
>>> print ('Greetings, ' + FirstName)
Greetings, Maxwell
>>> 
# Exercises for chapter 3:
Exercise 3.1
Move the last line of this program to the top, so the function call appears
before the definitions. Run the program and see what error message you get.

#When you move "repeat_lyrics()" to the top, this message appears:
#NameError: name 'repeat_lyrics' is not defined

Exercise 3.2
Move the function call back to the bottom and move the definition of print_lyrics
after the definition of repeat_lyrics. What happens when you run this program?

#def repeat_lyrics():
  print_lyrics()
  print_lyrics()
#def print_lyrics():
  print "I'm a lumberjack, and I'm okay."
  print "I sleep all night and I work all day."
repeat_lyrics

#I got the message: 
#File "<stdin>", line 4
#def print_lyrics():
   ^
#SyntaxError: invalid syntax

Exercise 3.3
Write a function named right_justify that takes a string named s as a parameter
and prints the string with enough leading spaces so that the last letter of the
string is in column 70 of the display.

def right_justify(s):

    right justify's'
    
#Is an indentation required here?
#When I try to define a function, I keep getting error messages "unexpected indentation block"
    (when tried with 5 spaces)
#Other error: "unexpected indent" when I use the tab key to indent the "right justify 's'" line
    
Exercise 3.4
1.Type this example into a script and test it. #It worked!!

>>> def do_twice(f):
	 f()
	 f()

	 
>>> def print_spam():
	 print 'spam'

	 
>>> do_twice(print_spam)
spam
spam
>>> 
#only put one space before entering function definitions (i.e. "f()" or "print 'spam'")

2.Modify do_twice so that it takes two arguments, a function object and a value,
and calls the function twice, passing the value as an argument.

def do_twice(f):
     f()
     f(x)

3. Write a more general version of print_spam called print_twice, that takes
a string as a parameter and prints it twice.

def print_twice(dumplings):
     print 'dumplings'
     print 'dumplings'
     
 #dumplings = parameter?

#Or:

def print_twice(<typ'str'>):
    print

4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.
def do_twice(f):
     f()
     f()
def print_twice(spam):
     print 'spam'
     print 'spam'

do_twice(print_twice(spam)

#when the above line is run, this error message appears:

    Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    do_twice(print_twice(spam))
NameError: name 'spam' is not defined

#If I run this:
>>> do_twice(print_twice)
#(No argument)

#I get this error message:

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    do_twice(print_twice)
  File "<pyshell#21>", line 2, in do_twice
    f()
TypeError: print_twice() takes exactly 1 argument (0 given)
>>> 
         

         


# Name: Lauren Dunn

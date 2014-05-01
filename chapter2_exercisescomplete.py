# Exercises for chapter 2:

Exercise 2.1
#Values 01, 010, 0100, and 01000 all come back as type(int) 
#Why doesn't this work for 02492?
-------------------------------------------------------
Exercise 2.2
#In the Python Interpreter:
5
x = 5
#x + 1 = 6

Putting Statements into a script yields the following results:
#File"<stdin>", line 1
#x+1=
    ^
#SyntaxError: invalid syntax

When modified into a print statement:
  
print 5 --> 5
x = 5
print x + 1 --> 6

#It displays the answer to the equation when prompted!
---------------------------------------------------------
Exercise 2.3

#Example given:
width= 17
height = 12.0
delimiter = '.'

1. width/2
# 17/2= 8
#print width/2
#solution is rounded and displayed as an interger or typ(int)

2. width/2.0
#17/2.0 = 8.5
#print width/2.0
#solution is displayed as a "floating point" or typ(float)

3. height/3
#12.0/3= 4.0
#print 12.0/3 = 4.0
#solution is displayed as a floating point

4. 1+2*5
print 1+2*5 --> 11
#PEMDAS
#2*5=10
#1+10=11

5. delimiter *5
#print delimiter *5
#.....
#multiplication or "*" symbol results in a character or phrase being repeated
-----------------------------------------------------------------------------
Exercise 2.4
1.The volume of a sphere with radius r is 4/3pir^3

#I got the right answer, but how to simplify into less steps?
#How do I get the pi symbol when coding?
#r=5
#print 3.14159*r**3=392.69875
#print 392.69875*4/3= 523.59833

#volume of sphere = approx 523

2.Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. 
Shipping costs $3 for the first copy and 75 cents for each additional copy. 
What is the total wholesale cost for 60 copies?

#book=24.95
#wholesalebook= book *.4

#Shipping = 3 + .75(number of books-1)
#Total wholesale cost for 60 copies:
#print wholesalebook*60+shipping

(24.95*.6)60 +3 +(.75*59)=945.45

3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

#convert minutes into decimals

#easypace=8.25
#tempo=7.20

easypace+(tempo*3)+easypace= 38.1 minutes = total time running

6:52 +38 minutes, 6 seconds =
#home at 7:30 am and 6 seconds  for breakfast

---------------------------------------------------------------------
---------------------------------------------------------------------
# Name: Lauren Dunn

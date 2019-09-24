#!/usr/bin/python3
#
#==============================================================================
# CSci 3003 -- Lab 1
# This is your first Python Script
#==============================================================================
#
#
# 

print("********************************************************************")
print("********************************************************************")
print("********************************************************************")
print("****               Welcome to Csci 3003                         ****")
print("********************************************************************")
print("********************************************************************")
print("********************************************************************")

# Comments go inside your script file. 
# They are useful for keeping notes!
# Use them to provide short answers to the questions below.
print("A line starting with an '#' is called a comment")
print("It is ignored by the computer.")
print("You can put whatever you want on the line!")
print("Use them to keep notes and track what you are doing!")
input("Press enter to continue...")
print("\n"*100)

#==============================================================================
# # Question 1:
# #    What does the print function do?
#==============================================================================
print("Please provide the following information:")
fname = input("First name: ")
lname = input("Last name: ")
email = input('Email address: ')
studentid = input('Student ID #: ')

#==============================================================================
# # Question 2:
# #    How is the input() function different than print()?
#==============================================================================
#

print("Thanks for the details ",fname,"!")
input("Press enter to continue...")
print("\n"*100)
print("The Print function normally prints to a special file called 'standard out,'")
print("which is attached to the screen. You can print to a normal file by specifying")
print("a file parameter in the print function. The file you print to first needs")
print("to be opened with the open function. The second argument to the open")
print("function is an r or w for reading or writing.")
input("Press Enter to Continue")
print("\n"*100)

print("Printing information to 'lab1_output.txt'")
infofile = open("lab1_output.txt",'w')
print("CSci 3003 Lab 1 info:", file=infofile)
print("Name: ",fname," ",lname,"\nemail: ",email,"\nstudentid: ",studentid, file=infofile)
infofile.close()
input("Press Enter to Continue")
print("\n"*100)

#==============================================================================
# # Question 3: 
# #    In the print statements above, what does the "\n" do?
#==============================================================================

#
#---------------------PYTHON DEMOS BELOW HERE---------------------------------
#
print("---------Data Types in Python--------------------------")
print("Python has several built in data types called primitives. Most")
print("functions are built around manipulating and keeping track of a few")
print("data primitives. Every value in python has a certain 'type' which ")
print("identifies the kind of value it is. For instance an integer versus a")
print("floating point number.")
input("Press Enter to Continue")
print("\n"*100)

print("---------Numbers in Python--------------------------")
print("Integer demo... ")
intA = 1
intB = 2
print("Integer A =", intA, " and IntegerB = ", intB)
intSum = intA + intB
print("Integer Sum: ",intSum)

print('float demo....')
floatA = 1.0
floatB = 2.0
print("FloatA =", floatA, "and floatB =", floatB)
floatSum = floatA + floatB
print("Float sum:", floatSum)

print('You can mix integers and floats!')
mixedSum = intA + floatA
print("Mixed Sum:",mixedSum)

print('You can use scientific notation to use REALLY BIG/small numbers:')
bigNumber = 4e5
tinyNumber = 4e-5
print("Scientific Notation: ",bigNumber+tinyNumber)

# Python will convert between number types on the fly!


input("Press Enter to Continue")
print("\n"*100)

print("---------Strings in Python--------------------------")
print("In python, a series of characters is called a string. While computers")
print("are very good at storing numbers, human readable types such as strings")
print("pose interesting problems. For instance, how should 'invisible' characters")
print("such as tabs or spaces be represented? Or when you hit 'enter', do you")
print("mean you want to finish a statement or have the string span multiple lines?\n\n")

print("Strings are represented with quotes. Anything within the quotes is ")
print("included in the string.\n\n")

print("String Demo....\n\n")
str1 = "This is one string."
print("String1:",str1,"\n\n")


print("Sometimes you want your string to span multiple lines")
print("This case is handled with triple quotes or by embedding the")
print("newline character: \\n")
print("\n")

# Multiline strings are easy to read!
str4 = '''This
String
Spans
Multiple
Lines'''
print("Multiline String:\n", str4,"\n\n")
input("Press Enter to Continue\n\n")

# Strings using the newline character are compact!
str5 = 'But\nso\ndoes\nthis\none'
print("Multiline String2 :\n",str5)
input("Press Enter to Continue\n\n")

# We will now switch to printing multiline statements using a single
# Print statement, making it more readable and requires less typing

print('''Sometimes you want to concatenate or 'add' strings together, 
python will happily do this with the plus operator. Just
remember to include the appropriate white space!\n''')

#          White space ---v
concatString = "hello" + " " + "world"
print("Concatenated String:", concatString)

# This makes it convenient to build 'easy to read' print statements:
print("Another Concatenated String: " + "hello world")


input("Press Enter to Continue")
print("\n"*100)



print("---------Expressions in Python--------------------------")

print("""Expressions are combinations of types that need to be calculated
using basic operations such as adding, subtracting or concatenating. We saw some
basic expressions above using numbers.\n\n""")

# Expression nested within functions are evaluated before being passed into the
# function making it possible to write concise, compound expressions.

#                                            Compound Expression ---
#                                                                __ |__
#                                                               /       \
print("You've seen numeric expressions before!: 100 + 100 == ", 100 + 100)

# We've seen basic strings expressions before too!
print("You've also seen string expressions ", "Be"+"fore"+"\n\n")

# There are also other operators that can act on strings
print("repeat!" * 10)

#==============================================================================
# # Question 4:
#   What have the following print statements been doing?
#   >>> print("\n" * 100)
#==============================================================================


print("There are also some other interesting string operations:")

# TATA Box Reference: http://en.wikipedia.org/wiki/TATA_box
print("Is there a TATA Box? ", 'TATA' in "TATATATATATATATATATATATA")
# GC Content Reference: http://en.wikipedia.org/wiki/GC_rich
print("Is there GC rich region?", "GC"*4 in "TAGCATGCGCGCGCGTACATAGCAGTA")
print("\n\n")


input("Press Enter to Continue")
print("\n"*100)


print("---------Built in Functions and Method Calls in Python--------------------------")
print("""Python has a set of built in functions that are commonly used in 
addition to the expressions we saw above. The most familiar function we have
dealt with so far has been print(). A function has a name and a pair of parentheses 
that contain zero or more arguments. These arguments are evaluated if they
are expressions and then the function does 'something', in this case prints the 
expression to the screen, and returns a value. Some other common python functions 
are len(), input(), abs(), max(), min(), and help(). \n\n""")

short_string = input("Input a short string:")
print("You typed ", len(short_string), "letters\n\n")

input("Press Enter to Continue")
print("\n"*100)

print("---------Built in Functions and Method Calls in Python--------------------------")
print("""Method calls are functions that are specific to a certain type and
are accessed using the dot operator. For example running: "hello world".count('l')
returns the number of times the character 'l' occurs in the string preceding
the dot. Other string methonds include string.find() string.startswith(), 
string.strip(), string.lstrip() and string.rstrip(). These methods can be used 
in conjunction with logical operators for instance from above to first test for 
occurances of a TATA box and then extract it with the slice operator.\n\n""")

print("String Method with logical operator Demo:")

nucleotides = 'AGACGATAGCCAAGATAATATAGCAAGACAAGTATAGA'
if 'TATA' in nucleotides:
    print("Found a promoter region in "+nucleotides)
    start_index = nucleotides.find('TATA')
    print("It starts at index " , start_index)
    end_index = len(nucleotides)
    print("and ends at index " , end_index)
    promoter_seq = nucleotides[start_index:end_index]
    print("Promoter sequence: " + promoter_seq)
else:
    print("Didn't find promoter sequence in " + nucleotides)

nucleotides2 = 'ACTAGAGATATCGCGCTAGAGCGCGCGATAGCGTGCTAGA'
if 'TATA' in nucleotides2:
    print("Found a promoter region in "+nucleotides2)
    start_index = nucleotides2.find('TATA')
    print("It starts at index " , start_index)
    end_index = len(nucleotides2)
    print("and ends at index " , end_index)
    promoter_seq = nucleotides2[start_index:end_index]
    print("Promoter sequence: " + promoter_seq)
else:
    print("Didn't find promoter sequence in " + nucleotides2)


input("Press Enter to Continue")
print("\n"*100)
#==============================================================================
# # Question 5:
#    What do you think the 'if' and 'else' keywords above are doing?
#==============================================================================


print("********************************************************************")
print("********************************************************************")
print("********************************************************************")
print("***          CONGRATULATIONS! You've finished lab1!              ***")
print("********************************************************************")
print("********************************************************************")
print("********************************************************************")

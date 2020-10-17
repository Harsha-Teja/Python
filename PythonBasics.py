# Day One

# Python is user friendly and easy to learn language. Best language to start your coding journey.
# The one main disdvantage of python is the execution time when compared to c, c++ or java. Making it difficult to use it in competetive programming.
# In mac there's an inbuilt version of python2 and we have to install python3 manually.
# Python is top-down therefore it always executes the lines from top to the bottom.

# Commenting in python is done in two types.
# 1) Adding an # symbol before an statement. This is a signle line comment
# 2) Inserting senteces between """ adding the statements here """ . This is an multi line commmet

# To print any thing in python we use the function call print('the statement here')
# Python's philosophy is " simplicity is the best"

# Python is an dynamiccally typed language: We dont have to mention about he variable type before hand as it will detect
#                                           the type upon assigning the variable value.
# Assigning a value is known as binding in Python

# In both the version of python2 and python3. The main difference is that the python 2 is based on ASCII and python 3 is based on Unicdoe
# ASCII -  ASCII codes represent text in computers, telecommunications equipment, and other devices.
# Unicode - Unicode is an information technology standard for the consistent encoding, representation, and handling of text expressed.

# Here are naming conventions for Python identifiers −
# Class names start with an uppercase letter. All other identifiers start with a lowercase letter.
# Starting an identifier with a single leading underscore indicates that the identifier is private.
# Starting an identifier with two leading underscores indicates a strongly private identifier.
# # If the identifier also ends with two trailing underscores, the identifier is a language-defined special name.

# Just like in ,any other languages python has its own set of keywords. To check which words are considered as python keywords we
# can use the module keyword. Then check using iskeyword("the word")
# Few key words in python:

# True
# False
# None
# and
# or
# not
# assert
# break
# continue
# class
# def
# if
# elif
# else
# del
# try
# except
# raise
# finally
# for
# while
# pass
# import
# as
# from
# in
# is
# return
# global
# non-local

# The namespaces and scope in python can be thought of as an venn diagram.

# Python stores the namespace scope in a python dictionary which gets updated accordingly

# The first and foremost region is of built-in namespaces like print()
# The second region is of global namspace which gets created once a module is created
# Then third region is of local namespace which has access within the object, either it being a class or a function.
# In Python, if-else and for/while loop block doesn’t create any local scope.

# Python does not allow punctuation characters such as @, $, and % within identifiers. Python is a case sensitive programming language.

# To write an multistatement lines in python we use two types of methods. Explicit and Implicit
# Explicit : we use an keyword "\" at the end of the line to continue the statement to next line
# Implicit : As most of the long statements prolong inside parentheses or {},(), [] brackets. We can extend the ending bracket to next lines as well.
# Decision making in python: Similar to real time scenarios if we want to make a decision based on the outcome of another conidtion.
#                             We use this category of parameters. Like, if, elif, else. which helps us to execute the statement based
#                             on whether the condition is true or not.

# There are two methods of taking input from the user in python dialogue box.
# 1) raw_input : This is the version used in python2 where the input value is considered as string and then typecasting is deon to convert it.
# 2) inupt() : This is version used in python3 where the input value is considered based on the value entered. Yet can be mentioned for validation.

# Multiple inputs can be taken from the user using two methods:
# 1) split  : x ,y = input(enter two numbers: ).split()
# 2) List comprehensions : user = [x for x in input(Enter the words).split()]

# In the python3 ( which will be considered as standard version in this joruney )
# We can modify the after action of print statement with an parameter called end.
# By default its value is new line /n but we can change it too 'space' or any other value.
# similar to the end parameter we can also use the parameter called 'sep' which have daulf value of space but can be modified wit hany keyword.

# Similar to the user input modifications there are also other methods to modify the user output functions. In python3
# 1) using the string moluo
# 2) using the format string
# 3) using the f string

# Python accepts single ('), double (") and triple (''' or """) quotes to denote string literals, as long as the same
#           type of quote starts and ends the string.
"""
print('Harsha has: %2d apple and : %3d oranges' % (4, 3))
print('I am from {} nice to {} you'.format('India', 'meet'))
name = 'harsha'
print(f'It was nice meeting you {name}')
"""

# The basic data types in python are:
# 1) int
# 2) string
# 3) boolean
# 4) float
# 5) complex
# 6) long
# The operations in python are:

# 1) Arithmetic Operators
# 2) Comparison (Relational) Operators
# 3) Assignment Operators
# 4) Logical Operators
# 5) Bitwise Operators
# 6) Membership Operators
# 7) Identity Operators

# Arithmetic Operators:

# a) addition ( + )
# b) subtraction ( - )
# c) divide ( / )
# d) multiply ( * )
# e) Modulus ( % )
# f) Exponent ( ** )
# g) Floor division ( // )

# Comparison Operators:

# a) == ( equal to )
# b) != also <> ( not equal to)
# c) >
# d) <
# e) >=
# f) <=

# Assignment Operators:

# a) =
# b) c+=a ( c= c +a )
# c) c-=a ( c = c -a )
# d) c -= a ( c = c - a )
# e) c *= a (c = c * a)
# f) c /= a ( c = c / a)
# g) c%= a ( c = c % a)
# h) c**=a (c = c ** a)
# i) c //= a (c = c //a )

# Logical Operators:

# a) AND
# b) OR
# c) Not

# Bitwise Operators: Bitwise operator works on bits and performs bit by bit operation.
#                 Assume if a = 60; and b = 13; Now in the binary format their values will be 0011 1100 and 0000 1101

#  a) & ( AND in binary a and b )
#  b) \ ( OR in binary a or b)

# Membership operators:
# a) in
# b) not in

# Identity Operators:
# a) is
# b) is not
"""
The frozenset() method returns an immutable frozenset object initialized with elements from the given iterable. 
Frozen set is just an immutable version of a Python set object. 
While elements of a set can be modified at any time, elements of frozen set remains the same after creation.
"""

#### Importing modules
######################
######################
import re # will need to prefix
my_regex = re.compile('[0-9]+', re.I)

import re as regex # alias
my_regex = regex.compile('[0-9]+', re.I)

from collections import defaultdict, Counter # import explicit values
lookup = defaultdict(int) # does not require qualification:

from re import * # bad practice, don't do this. overwrites vars

#### Append to a list
######################
######################
x = [1, 2, 3]
x.append(0)

#### Tuples
######################
######################

# immutable cousin of lists
my_list = [1, 2]
my_tuple = (1, 2)
my_list[1] = 3 # my_list is now [1,3]
# my_tuple[1] = 3 # cannot do this

#### defaultdict
######################
######################
from collections import defaultdict
# when you try to look up a key it doesn't contain, it first adds a value for 
# it using a zero-argument function you provided when you created it
# as opposed to a dict, which will throw an error if looking up a key that is 
# not in the dict

# An example of a situation where this would be useful:
word_counts = defaultdict(0)
for word in document:
    word_counts[word] +=1

#### Single line if-else statement
######################
######################
parity = 'even' if x % 2 == 0 else 'odd'

#### List comprehensions
######################
######################
# transform a list into another list
even_numbers = [x for x in range(5) if x % 2 == 0] # [0, 2, 4]

#### Generator (yield)
######################
######################
# something you can iterate over but whose values are producted only as needed
# i.e. lazily
# compare to range(1000000), which creates a list of 1M elements
def lazy_range(n):
    '''a lazy version of range'''
    i = 0
    while i < n:
        yield i
        i += 1

#### Generate random numbers
######################
######################
import random
random.seed(10)
print random.random()
random.randrange(10) # chooses randomly from range(10)
random.shuffle(range(10)) # randomly reorders elements of a list

#### enumerate
######################
######################
# iterate over a list and use both its elements and their indexes
# very handy!
# not pythonic:
for i range(len(documents)):
    documents = documents[i]
    do_something(, document)

# also not pythonic
i = 0
for document in documents:
    do_something(i, documents)
    i += 1

# pythonic:
for i, document in enumerate(documents):
    do_something(i, document)

#### zip
######################
###################### 
# transforms multiple lists into a single list of tupes of corresponding elements
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zip(list1, list2) # [('a', 1), ('b', 2), ('c', 3)]

# args and kwargs
######################
######################
# specify a function that takes arbitrary arguments
# useful in creating higher-order functions
def f2(x, y):
    return x + y

def doubler_correct(f):
    '''works no matter what kind of inputs f expects'''
    def g(*args, **kwargs):
        '''whatever arguments g is suuplied, pass through to f'''
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
print(g(1, 2)) # 6

#### Lambdas 
######################
######################
# Lambas are short, anonymous functions.
# They are sorta hard to grok and I probably won't need to much for data
# science code. 
# Read this if I need to re-learn them in the future:
# https://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/


#### Style
######################
######################
# use 4 spaces for indentation
 
# surround top-level functions and class definitions with two blank lines

# methods inside of a class get one blank line

# group imports in the order: standard lib, third party, local

# with a line between each group

# avoid extraneous whitespace, e.g.:
spam(ham[1], (eggs: 2)) # yes
spam( ham[ 1 ], ( eggs: 2 ) ) # no
 
# binary operations should have a single space on either side (=,<,>,+, etc.)
# but, don't use spaces around keyword arguments
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# Commens should be complete sentances. First word should be capitalized, unless
# it is referring to an identifer that begins with a lower-case letter

# Use inline comments sparingly. Seperate by at least two-spaces.
    
# When writing docstrings, closing quote (""") should be on its own line, unless
# its a one-liner docstring. 
    
# Functions should be lowercase, with words seperated by underscores.
# Variable names follow the same convention as functions.
# Classes use capitals: MyClass
# Don't use mixedCase.
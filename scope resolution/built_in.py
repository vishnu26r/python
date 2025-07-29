
#this is built-in scope ,but it will 1st check for the local scope 
from math import e


def func1():
    print(e)

e=3
func1()
import operator as op
from functools import reduce
from googletrans import Translator
import sys

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom
	
def check_if_module_imported(modulename):
	return modulename in sys.modules
	
	
"""
add latex to text 
add text to latex
add function that operates on equation and spits out latex
"""

translator = Translator()
def trans(word):
    print(translator.translate(word).text)


while True:
    command = input("enter command\n")
    if command == 't':
        while command != 'e':
            trans(input("enter word to translate\n"))

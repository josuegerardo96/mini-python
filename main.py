# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from miParserLexer import *
from miParserParser import *
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from AContextual import *
#from pyInterLexer import *
#from pyInterParser import *




def main():
    input = FileStream('test.txt')
    lexer = miParserLexer(input)
    #lexer.removeErrorListeners()
    #lexer.addErrorListener(MyErrorListener())
    #lexer._listeners = [ MyErrorListener() ]
    stream = CommonTokenStream(lexer)

    parser = miParserParser(stream)
    #parser.removeErrorListeners()
    #parser.addErrorListener(MyErrorListener())

    tree = parser.program()
    v = AContextual()
    v.visit(tree)


if __name__ == '__main__':
    main()
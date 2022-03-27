# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from miParserLexer import *
from miParserParser import *
from antlr4 import *

def main():
    input = FileStream('test.txt')
    lexer = miParserLexer(input)
    stream = CommonTokenStream(lexer)
    parser = miParserParser(stream)
    tree = parser.program()
if __name__ == '__main__':
    main()
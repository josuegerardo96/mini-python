# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from miParserLexer import *
from miParserParser import *
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from AContextual import *
from codeGen import  codeGen
import os
import sys
#from pyInterLexer import *
#from pyInterParser import *

def generar_bytecode(codigo):
    f = open('bytecode.txt', 'w')
    cont = 0
    for instr in codigo:
        if (instr.arg == None):
            f.write("{} {}\n".format(str(cont), instr.instr))
        else:
            f.write("{} {} {}\n".format(str(cont), instr.instr, instr.arg))
        cont += 1
    f.close()


def main():
    input = FileStream('texto.txt')
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
    v2= codeGen()
    generar_bytecode(v2.visit(tree))
    v.printErrors()
    #os.system("MiniPy bytecode.txt")

if __name__ == '__main__':
    main()
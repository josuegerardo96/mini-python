# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from miParserLexer import *
from miParserParser import *
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener


class MyErrorListener( ErrorListener ):

    sys.tracebacklimit = -1
    def __init__(self):
        super(MyErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if(recognizer.__eq__(Lexer)):
            raise Exception("Syntax Error Lexer!!")
        else:
            raise Exception("Syntax Error Parser!!")

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        if (recognizer.__eq__(Lexer)):
            raise Exception("Ambiguity Lexer!!")
        else:
            raise Exception("Ambiguity Parser!!")

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        if (recognizer.__eq__(Lexer)):
            raise Exception("Attempting Full Context Lexer!!")
        else:
            raise Exception("Attempting Full Context Parser!!")

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        if (recognizer.__eq__(Lexer)):
            raise Exception("Context Sensitivity Lexer!!")
        else:
            raise Exception("Context Sensitivity Parser!!")

    def reportLexerNoViableAltException(self, recognizer, dfa, startIndex, stopIndex,configs):
            raise Exception("LexerNoViableAltException")




def main():
    input = FileStream('test.txt')
    lexer = miParserLexer(input)
    lexer.removeErrorListeners()
    lexer.addErrorListener(MyErrorListener())
    #lexer._listeners = [ MyErrorListener() ]
    stream = CommonTokenStream(lexer)

    parser = miParserParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(MyErrorListener())

    tree = parser.program()
if __name__ == '__main__':
    main()
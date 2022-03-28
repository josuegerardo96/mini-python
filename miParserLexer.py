# Generated from C:/Users/Meih55/Desktop/mini-python\miParser.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from antlr_denter.DenterHelper import DenterHelper
from miParserParser import miParserParser



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2$")
        buf.write("\u00f5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3")
        buf.write("\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\7\33\u00a0\n\33\f\33\16\33\u00a3\13\33\3\34")
        buf.write("\6\34\u00a6\n\34\r\34\16\34\u00a7\3\35\6\35\u00ab\n\35")
        buf.write("\r\35\16\35\u00ac\3\35\3\35\6\35\u00b1\n\35\r\35\16\35")
        buf.write("\u00b2\3\36\3\36\3\36\3\36\3\36\7\36\u00ba\n\36\f\36\16")
        buf.write("\36\u00bd\13\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\5\37\u00c8\n\37\3\37\3\37\3 \3 \7 \u00ce\n \f \16")
        buf.write(" \u00d1\13 \3 \3 \3!\3!\3\"\5\"\u00d8\n\"\3#\3#\3$\3$")
        buf.write("\3$\3%\5%\u00e0\n%\3%\3%\7%\u00e4\n%\f%\16%\u00e7\13%")
        buf.write("\3&\3&\7&\u00eb\n&\f&\16&\u00ee\13&\3&\3&\3\'\3\'\3\'")
        buf.write("\3\'\4\u00bb\u00cf\2(\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\2C\2E\2G\2I\"K#M$\3\2\t\3\2\62;\5\2C\\aac|\6\2\f")
        buf.write("\f\17\17))^^\n\2$$))^^ddhhppttvv\4\2\13\13\"\"\4\2\f\f")
        buf.write("\16\17\6\2\13\f\17\17\"\"--\2\u00fb\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2I\3\2\2\2\2K\3\2")
        buf.write("\2\2\2M\3\2\2\2\3O\3\2\2\2\5Q\3\2\2\2\7S\3\2\2\2\tU\3")
        buf.write("\2\2\2\13W\3\2\2\2\rY\3\2\2\2\17[\3\2\2\2\21^\3\2\2\2")
        buf.write("\23a\3\2\2\2\25d\3\2\2\2\27f\3\2\2\2\31h\3\2\2\2\33j\3")
        buf.write("\2\2\2\35l\3\2\2\2\37n\3\2\2\2!p\3\2\2\2#r\3\2\2\2%u\3")
        buf.write("\2\2\2\'z\3\2\2\2)\u0080\3\2\2\2+\u0084\3\2\2\2-\u0087")
        buf.write("\3\2\2\2/\u008e\3\2\2\2\61\u0094\3\2\2\2\63\u0098\3\2")
        buf.write("\2\2\65\u009c\3\2\2\2\67\u00a5\3\2\2\29\u00aa\3\2\2\2")
        buf.write(";\u00b4\3\2\2\2=\u00c4\3\2\2\2?\u00cb\3\2\2\2A\u00d4\3")
        buf.write("\2\2\2C\u00d7\3\2\2\2E\u00d9\3\2\2\2G\u00db\3\2\2\2I\u00df")
        buf.write("\3\2\2\2K\u00e8\3\2\2\2M\u00f1\3\2\2\2OP\7*\2\2P\4\3\2")
        buf.write("\2\2QR\7+\2\2R\6\3\2\2\2ST\7<\2\2T\b\3\2\2\2UV\7.\2\2")
        buf.write("V\n\3\2\2\2WX\7@\2\2X\f\3\2\2\2YZ\7>\2\2Z\16\3\2\2\2[")
        buf.write("\\\7>\2\2\\]\7?\2\2]\20\3\2\2\2^_\7@\2\2_`\7?\2\2`\22")
        buf.write("\3\2\2\2ab\7?\2\2bc\7?\2\2c\24\3\2\2\2de\7-\2\2e\26\3")
        buf.write("\2\2\2fg\7/\2\2g\30\3\2\2\2hi\7?\2\2i\32\3\2\2\2jk\7,")
        buf.write("\2\2k\34\3\2\2\2lm\7\61\2\2m\36\3\2\2\2no\7]\2\2o \3\2")
        buf.write("\2\2pq\7_\2\2q\"\3\2\2\2rs\7k\2\2st\7h\2\2t$\3\2\2\2u")
        buf.write("v\7g\2\2vw\7n\2\2wx\7u\2\2xy\7g\2\2y&\3\2\2\2z{\7y\2\2")
        buf.write("{|\7j\2\2|}\7k\2\2}~\7n\2\2~\177\7g\2\2\177(\3\2\2\2\u0080")
        buf.write("\u0081\7h\2\2\u0081\u0082\7q\2\2\u0082\u0083\7t\2\2\u0083")
        buf.write("*\3\2\2\2\u0084\u0085\7k\2\2\u0085\u0086\7p\2\2\u0086")
        buf.write(",\3\2\2\2\u0087\u0088\7t\2\2\u0088\u0089\7g\2\2\u0089")
        buf.write("\u008a\7v\2\2\u008a\u008b\7w\2\2\u008b\u008c\7t\2\2\u008c")
        buf.write("\u008d\7p\2\2\u008d.\3\2\2\2\u008e\u008f\7r\2\2\u008f")
        buf.write("\u0090\7t\2\2\u0090\u0091\7k\2\2\u0091\u0092\7p\2\2\u0092")
        buf.write("\u0093\7v\2\2\u0093\60\3\2\2\2\u0094\u0095\7f\2\2\u0095")
        buf.write("\u0096\7g\2\2\u0096\u0097\7h\2\2\u0097\62\3\2\2\2\u0098")
        buf.write("\u0099\7n\2\2\u0099\u009a\7g\2\2\u009a\u009b\7p\2\2\u009b")
        buf.write("\64\3\2\2\2\u009c\u00a1\5C\"\2\u009d\u00a0\5C\"\2\u009e")
        buf.write("\u00a0\5A!\2\u009f\u009d\3\2\2\2\u009f\u009e\3\2\2\2\u00a0")
        buf.write("\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2")
        buf.write("\u00a2\66\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a6\5A!")
        buf.write("\2\u00a5\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a5")
        buf.write("\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a88\3\2\2\2\u00a9\u00ab")
        buf.write("\5A!\2\u00aa\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2\u00ac\u00aa")
        buf.write("\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae")
        buf.write("\u00b0\7\60\2\2\u00af\u00b1\5A!\2\u00b0\u00af\3\2\2\2")
        buf.write("\u00b1\u00b2\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3")
        buf.write("\2\2\2\u00b3:\3\2\2\2\u00b4\u00b5\7$\2\2\u00b5\u00b6\7")
        buf.write("$\2\2\u00b6\u00b7\7$\2\2\u00b7\u00bb\3\2\2\2\u00b8\u00ba")
        buf.write("\13\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\u00bd\3\2\2\2\u00bb")
        buf.write("\u00bc\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bc\u00be\3\2\2\2")
        buf.write("\u00bd\u00bb\3\2\2\2\u00be\u00bf\7$\2\2\u00bf\u00c0\7")
        buf.write("$\2\2\u00c0\u00c1\7$\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3")
        buf.write("\b\36\2\2\u00c3<\3\2\2\2\u00c4\u00c7\7)\2\2\u00c5\u00c8")
        buf.write("\5E#\2\u00c6\u00c8\5G$\2\u00c7\u00c5\3\2\2\2\u00c7\u00c6")
        buf.write("\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00ca\7)\2\2\u00ca")
        buf.write(">\3\2\2\2\u00cb\u00cf\7$\2\2\u00cc\u00ce\13\2\2\2\u00cd")
        buf.write("\u00cc\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00d0\3\2\2\2")
        buf.write("\u00cf\u00cd\3\2\2\2\u00d0\u00d2\3\2\2\2\u00d1\u00cf\3")
        buf.write("\2\2\2\u00d2\u00d3\7$\2\2\u00d3@\3\2\2\2\u00d4\u00d5\t")
        buf.write("\2\2\2\u00d5B\3\2\2\2\u00d6\u00d8\t\3\2\2\u00d7\u00d6")
        buf.write("\3\2\2\2\u00d8D\3\2\2\2\u00d9\u00da\n\4\2\2\u00daF\3\2")
        buf.write("\2\2\u00db\u00dc\7^\2\2\u00dc\u00dd\t\5\2\2\u00ddH\3\2")
        buf.write("\2\2\u00de\u00e0\7\17\2\2\u00df\u00de\3\2\2\2\u00df\u00e0")
        buf.write("\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e5\7\f\2\2\u00e2")
        buf.write("\u00e4\t\6\2\2\u00e3\u00e2\3\2\2\2\u00e4\u00e7\3\2\2\2")
        buf.write("\u00e5\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6J\3\2\2")
        buf.write("\2\u00e7\u00e5\3\2\2\2\u00e8\u00ec\7%\2\2\u00e9\u00eb")
        buf.write("\n\7\2\2\u00ea\u00e9\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec")
        buf.write("\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ef\3\2\2\2")
        buf.write("\u00ee\u00ec\3\2\2\2\u00ef\u00f0\b&\2\2\u00f0L\3\2\2\2")
        buf.write("\u00f1\u00f2\t\b\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4\b")
        buf.write("\'\2\2\u00f4N\3\2\2\2\17\2\u009f\u00a1\u00a7\u00ac\u00b2")
        buf.write("\u00bb\u00c7\u00cf\u00d7\u00df\u00e5\u00ec\3\b\2\2")
        return buf.getvalue()


class miParserLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PIZQ = 1
    PDER = 2
    DOSPUNT = 3
    COMA = 4
    MAYOR = 5
    MENOR = 6
    MAYORIGUAL = 7
    MENORIGUAL = 8
    IGUAL = 9
    MAS = 10
    MENOS = 11
    ASIGNACION = 12
    MULT = 13
    DIV = 14
    P2IZQ = 15
    P2DER = 16
    IF = 17
    ELSE = 18
    WHILE = 19
    FOR = 20
    IN = 21
    RETURN = 22
    PRINT = 23
    DEF = 24
    LEN = 25
    IDENTIFIER = 26
    INTEGER = 27
    FLOAT = 28
    COMMENTBLOCK = 29
    CHARCONST = 30
    STRING = 31
    NEWLINE = 32
    SINGCOMMENT = 33
    WS = 34

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "':'", "','", "'>'", "'<'", "'<='", "'>='", "'=='", 
            "'+'", "'-'", "'='", "'*'", "'/'", "'['", "']'", "'if'", "'else'", 
            "'while'", "'for'", "'in'", "'return'", "'print'", "'def'", 
            "'len'" ]

    symbolicNames = [ "<INVALID>",
            "PIZQ", "PDER", "DOSPUNT", "COMA", "MAYOR", "MENOR", "MAYORIGUAL", 
            "MENORIGUAL", "IGUAL", "MAS", "MENOS", "ASIGNACION", "MULT", 
            "DIV", "P2IZQ", "P2DER", "IF", "ELSE", "WHILE", "FOR", "IN", 
            "RETURN", "PRINT", "DEF", "LEN", "IDENTIFIER", "INTEGER", "FLOAT", 
            "COMMENTBLOCK", "CHARCONST", "STRING", "NEWLINE", "SINGCOMMENT", 
            "WS" ]

    ruleNames = [ "PIZQ", "PDER", "DOSPUNT", "COMA", "MAYOR", "MENOR", "MAYORIGUAL", 
                  "MENORIGUAL", "IGUAL", "MAS", "MENOS", "ASIGNACION", "MULT", 
                  "DIV", "P2IZQ", "P2DER", "IF", "ELSE", "WHILE", "FOR", 
                  "IN", "RETURN", "PRINT", "DEF", "LEN", "IDENTIFIER", "INTEGER", 
                  "FLOAT", "COMMENTBLOCK", "CHARCONST", "STRING", "DIGIT", 
                  "LETTER", "SINGLECHARACTER", "ESCAPESEQUENCE", "NEWLINE", 
                  "SINGCOMMENT", "WS" ]

    grammarFileName = "miParser.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    class MyCoolDenter(DenterHelper):
        def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
            super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
            self.lexer: miParserLexer = lexer

        def pull_token(self):
            return super(miParserLexer, self.lexer).nextToken()

    denter = None

    def nextToken(self):
        if not self.denter:
            self.denter = self.MyCoolDenter(self, self.NEWLINE, miParserParser.INDENT, miParserParser.DEDENT, False)
        return self.denter.next_token()



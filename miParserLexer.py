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
        buf.write("\4&\t&\4\'\t\'\4(\t(\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3")
        buf.write("\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\7\33\u00a2\n\33\f\33\16\33\u00a5\13\33")
        buf.write("\3\34\6\34\u00a8\n\34\r\34\16\34\u00a9\3\35\6\35\u00ad")
        buf.write("\n\35\r\35\16\35\u00ae\3\35\3\35\6\35\u00b3\n\35\r\35")
        buf.write("\16\35\u00b4\3\36\3\36\3\36\5\36\u00ba\n\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\7\37\u00c3\n\37\f\37\16\37\u00c6")
        buf.write("\13\37\3\37\3\37\3\37\3\37\3 \3 \7 \u00ce\n \f \16 \u00d1")
        buf.write("\13 \3 \3 \3!\3!\3\"\3\"\7\"\u00d9\n\"\f\"\16\"\u00dc")
        buf.write("\13\"\3#\3#\3$\5$\u00e1\n$\3%\3%\3&\3&\3&\3\'\5\'\u00e9")
        buf.write("\n\'\3\'\3\'\7\'\u00ed\n\'\f\'\16\'\u00f0\13\'\3(\3(\3")
        buf.write("(\3(\4\u00c4\u00cf\2)\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C\2E\2G\2I\2K\2M#O$\3\2\t\4\2\f\f\16\17\3\2\62")
        buf.write(";\4\2aac|\6\2\f\f\17\17))^^\n\2$$))^^ddhhppttvv\4\2\13")
        buf.write("\13\"\"\6\2\13\f\17\17\"\"--\2\u00fa\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\3Q\3\2\2\2\5S\3\2\2\2\7U\3\2\2\2\tW\3")
        buf.write("\2\2\2\13Y\3\2\2\2\r[\3\2\2\2\17]\3\2\2\2\21`\3\2\2\2")
        buf.write("\23c\3\2\2\2\25f\3\2\2\2\27h\3\2\2\2\31j\3\2\2\2\33l\3")
        buf.write("\2\2\2\35n\3\2\2\2\37p\3\2\2\2!r\3\2\2\2#t\3\2\2\2%w\3")
        buf.write("\2\2\2\'|\3\2\2\2)\u0082\3\2\2\2+\u0086\3\2\2\2-\u0089")
        buf.write("\3\2\2\2/\u0090\3\2\2\2\61\u0096\3\2\2\2\63\u009a\3\2")
        buf.write("\2\2\65\u009e\3\2\2\2\67\u00a7\3\2\2\29\u00ac\3\2\2\2")
        buf.write(";\u00b6\3\2\2\2=\u00bd\3\2\2\2?\u00cb\3\2\2\2A\u00d4\3")
        buf.write("\2\2\2C\u00d6\3\2\2\2E\u00dd\3\2\2\2G\u00e0\3\2\2\2I\u00e2")
        buf.write("\3\2\2\2K\u00e4\3\2\2\2M\u00e8\3\2\2\2O\u00f1\3\2\2\2")
        buf.write("QR\7*\2\2R\4\3\2\2\2ST\7+\2\2T\6\3\2\2\2UV\7<\2\2V\b\3")
        buf.write("\2\2\2WX\7.\2\2X\n\3\2\2\2YZ\7@\2\2Z\f\3\2\2\2[\\\7>\2")
        buf.write("\2\\\16\3\2\2\2]^\7>\2\2^_\7?\2\2_\20\3\2\2\2`a\7@\2\2")
        buf.write("ab\7?\2\2b\22\3\2\2\2cd\7?\2\2de\7?\2\2e\24\3\2\2\2fg")
        buf.write("\7-\2\2g\26\3\2\2\2hi\7/\2\2i\30\3\2\2\2jk\7?\2\2k\32")
        buf.write("\3\2\2\2lm\7,\2\2m\34\3\2\2\2no\7\61\2\2o\36\3\2\2\2p")
        buf.write("q\7]\2\2q \3\2\2\2rs\7_\2\2s\"\3\2\2\2tu\7k\2\2uv\7h\2")
        buf.write("\2v$\3\2\2\2wx\7g\2\2xy\7n\2\2yz\7u\2\2z{\7g\2\2{&\3\2")
        buf.write("\2\2|}\7y\2\2}~\7j\2\2~\177\7k\2\2\177\u0080\7n\2\2\u0080")
        buf.write("\u0081\7g\2\2\u0081(\3\2\2\2\u0082\u0083\7h\2\2\u0083")
        buf.write("\u0084\7q\2\2\u0084\u0085\7t\2\2\u0085*\3\2\2\2\u0086")
        buf.write("\u0087\7k\2\2\u0087\u0088\7p\2\2\u0088,\3\2\2\2\u0089")
        buf.write("\u008a\7t\2\2\u008a\u008b\7g\2\2\u008b\u008c\7v\2\2\u008c")
        buf.write("\u008d\7w\2\2\u008d\u008e\7t\2\2\u008e\u008f\7p\2\2\u008f")
        buf.write(".\3\2\2\2\u0090\u0091\7r\2\2\u0091\u0092\7t\2\2\u0092")
        buf.write("\u0093\7k\2\2\u0093\u0094\7p\2\2\u0094\u0095\7v\2\2\u0095")
        buf.write("\60\3\2\2\2\u0096\u0097\7f\2\2\u0097\u0098\7g\2\2\u0098")
        buf.write("\u0099\7h\2\2\u0099\62\3\2\2\2\u009a\u009b\7n\2\2\u009b")
        buf.write("\u009c\7g\2\2\u009c\u009d\7p\2\2\u009d\64\3\2\2\2\u009e")
        buf.write("\u00a3\5G$\2\u009f\u00a2\5G$\2\u00a0\u00a2\5E#\2\u00a1")
        buf.write("\u009f\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\u00a5\3\2\2\2")
        buf.write("\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\66\3\2")
        buf.write("\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a8\5E#\2\u00a7\u00a6")
        buf.write("\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9")
        buf.write("\u00aa\3\2\2\2\u00aa8\3\2\2\2\u00ab\u00ad\5E#\2\u00ac")
        buf.write("\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\u00ac\3\2\2\2")
        buf.write("\u00ae\u00af\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b2\7")
        buf.write("\60\2\2\u00b1\u00b3\5E#\2\u00b2\u00b1\3\2\2\2\u00b3\u00b4")
        buf.write("\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5")
        buf.write(":\3\2\2\2\u00b6\u00b9\7)\2\2\u00b7\u00ba\5I%\2\u00b8\u00ba")
        buf.write("\5K&\2\u00b9\u00b7\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\u00bb")
        buf.write("\3\2\2\2\u00bb\u00bc\7)\2\2\u00bc<\3\2\2\2\u00bd\u00be")
        buf.write("\7$\2\2\u00be\u00bf\7$\2\2\u00bf\u00c0\7$\2\2\u00c0\u00c4")
        buf.write("\3\2\2\2\u00c1\u00c3\13\2\2\2\u00c2\u00c1\3\2\2\2\u00c3")
        buf.write("\u00c6\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c4\u00c2\3\2\2\2")
        buf.write("\u00c5\u00c7\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00c8\7")
        buf.write("$\2\2\u00c8\u00c9\7$\2\2\u00c9\u00ca\7$\2\2\u00ca>\3\2")
        buf.write("\2\2\u00cb\u00cf\7$\2\2\u00cc\u00ce\13\2\2\2\u00cd\u00cc")
        buf.write("\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00d0\3\2\2\2\u00cf")
        buf.write("\u00cd\3\2\2\2\u00d0\u00d2\3\2\2\2\u00d1\u00cf\3\2\2\2")
        buf.write("\u00d2\u00d3\7$\2\2\u00d3@\3\2\2\2\u00d4\u00d5\5C\"\2")
        buf.write("\u00d5B\3\2\2\2\u00d6\u00da\7%\2\2\u00d7\u00d9\n\2\2\2")
        buf.write("\u00d8\u00d7\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3")
        buf.write("\2\2\2\u00da\u00db\3\2\2\2\u00dbD\3\2\2\2\u00dc\u00da")
        buf.write("\3\2\2\2\u00dd\u00de\t\3\2\2\u00deF\3\2\2\2\u00df\u00e1")
        buf.write("\t\4\2\2\u00e0\u00df\3\2\2\2\u00e1H\3\2\2\2\u00e2\u00e3")
        buf.write("\n\5\2\2\u00e3J\3\2\2\2\u00e4\u00e5\7^\2\2\u00e5\u00e6")
        buf.write("\t\6\2\2\u00e6L\3\2\2\2\u00e7\u00e9\7\17\2\2\u00e8\u00e7")
        buf.write("\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea")
        buf.write("\u00ee\7\f\2\2\u00eb\u00ed\t\7\2\2\u00ec\u00eb\3\2\2\2")
        buf.write("\u00ed\u00f0\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3")
        buf.write("\2\2\2\u00efN\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f1\u00f2")
        buf.write("\t\b\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4\b(\2\2\u00f4")
        buf.write("P\3\2\2\2\17\2\u00a1\u00a3\u00a9\u00ae\u00b4\u00b9\u00c4")
        buf.write("\u00cf\u00da\u00e0\u00e8\u00ee\3\b\2\2")
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
    CHARCONST = 29
    COMMENTBLOCK = 30
    STRING = 31
    SINGCOMMENT = 32
    NEWLINE = 33
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
            "CHARCONST", "COMMENTBLOCK", "STRING", "SINGCOMMENT", "NEWLINE", 
            "WS" ]

    ruleNames = [ "PIZQ", "PDER", "DOSPUNT", "COMA", "MAYOR", "MENOR", "MAYORIGUAL", 
                  "MENORIGUAL", "IGUAL", "MAS", "MENOS", "ASIGNACION", "MULT", 
                  "DIV", "P2IZQ", "P2DER", "IF", "ELSE", "WHILE", "FOR", 
                  "IN", "RETURN", "PRINT", "DEF", "LEN", "IDENTIFIER", "INTEGER", 
                  "FLOAT", "CHARCONST", "COMMENTBLOCK", "STRING", "SINGCOMMENT", 
                  "COMMENT", "DIGIT", "LETTER", "SINGLECHARACTER", "ESCAPESEQUENCE", 
                  "NEWLINE", "WS" ]

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



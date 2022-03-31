grammar miParser;

tokens { INDENT , DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from miParserParser import miParserParser
}
@lexer::members {
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
}

program : statement+;

statement: defStatement | ifStatement |returnStatement | printStatement |
whileStatement | forStatement | assignStatement | functionCallStatement |
expressionStatement;

defStatement: DEF IDENTIFIER PIZQ (argList?) PDER DOSPUNT sequence;

argList: IDENTIFIER (COMA IDENTIFIER)*;

moreArgs: (COMA IDENTIFIER)*;

ifStatement: IF expression DOSPUNT sequence (ELSE DOSPUNT sequence)?;

whileStatement: WHILE expression DOSPUNT sequence;

forStatement: FOR expression IN expressionList DOSPUNT sequence;

returnStatement: RETURN expression NEWLINE;

printStatement: PRINT expression NEWLINE;

assignStatement: IDENTIFIER ASIGNACION expression NEWLINE;

functionCallStatement: primitiveExpression PIZQ expressionList PDER NEWLINE;

expressionStatement: expressionList NEWLINE;

sequence: INDENT moreStatements DEDENT;

moreStatements: statement moreStatements*;

expression: additionExpression comparison;

comparison: ((MENOR | MAYOR | MAYORIGUAL | MENORIGUAL | IGUAL)additionExpression)* ;

additionExpression: multiplicationExpression additionFactor;

additionFactor: ((MAS | MENOS) multiplicationExpression)*;

multiplicationExpression: elementExpression multiplicationFactor;

multiplicationFactor: (( MULT | DIV ) elementExpression)*;

elementExpression: primitiveExpression elementAccess;

elementAccess: (P2IZQ expression P2DER)*;

expressionList: expression moreExpressions;

moreExpressions: (COMA expression)*;

primitiveExpression: '-'?INTEGER | '-'?FLOAT | CHARCONST | STRING | IDENTIFIER (PIZQ expressionList PDER|) | PIZQ expression
PDER | listExpression | LEN PIZQ expression PDER;

listExpression: P2IZQ expressionList P2DER;




//statement: def identifier (  identifier Arglist | //Epsilon    ) : INDENT MoreStatements DEDENT
//;

//simbolos
PIZQ : '(' ;
PDER : ')';
DOSPUNT : ':';
COMA : ',';
MAYOR : '>';
MENOR : '<';
MAYORIGUAL: '<=';
MENORIGUAL: '>=';
IGUAL: '==';           //Cambiar orden si da error
MAS : '+';
MENOS: '-';
ASIGNACION: '=';
MULT : '*';
DIV : '/' ;
P2IZQ : '[';
P2DER : ']';

//palabras reservadas
IF : 'if';
ELSE : 'else';
WHILE : 'while';
FOR : 'for';
IN : 'in';
RETURN : 'return';
PRINT : 'print';
DEF : 'def' ;
LEN : 'len';

//otros tokens
IDENTIFIER : LETTER (LETTER | DIGIT)*;
INTEGER : DIGIT+;
FLOAT: DIGIT + '.'  DIGIT+; //Describirlo en la documentacion
COMMENTBLOCK : '"""' .*? '"""' ->skip; //probar (adaptado del String)
CHARCONST : '\'' (SINGLECHARACTER | ESCAPESEQUENCE) '\''; //probar
STRING : '"' .*? '"' ; //probar


fragment DIGIT : [0-9];
fragment LETTER : '_'|[a-z]|[A-Z];
fragment SINGLECHARACTER:	~['\\\r\n]; //r return / n enter
fragment ESCAPESEQUENCE 	:	'\\' [btnfr"'\\];



NEWLINE: ('\r'? '\n' (' ' | '\t')*); //For tabs just switch out ' '* with '\t'*
SINGCOMMENT: '#' ~[\r\n\f]*->skip;
WS  :   [ +\r\n\t] -> skip ;

/**Referencias
http://kedizheng.com/2019/03/31/learning-antlr-4-building-grammar/
https://stackabuse.com/commenting-python-code/
Recognizer es instancia de Scanner o Parser
Si la lista es vacia= compilacion exitosa
Si es llena= compilacion fallida
**/


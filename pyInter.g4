grammar pyInter;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from pyInterParser import pyInterParser
}
@lexer::members {
class MiniPyDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: pyInterLexer = lexer

    def pull_token(self):
        return super(pyInterLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.MiniPyDenter(self, self.NEWLINE, pyInterParser.INDENT, pyInterParser.DEDENT, False)
    return self.denter.next_token()

}

program : statements;
statements : statement+;
statement : defStatement | ifStatement | returnStatement | printStatement | whileStatement | forStatement | assignStatement | functionCallStatement | expressionStatement ;
defStatement : DEF IDENTIFIER LEFTPARENT argList RIGTHPARENT COLON sequence ;
argList : IDENTIFIER ( COMMA IDENTIFIER)* ;
ifStatement : IF expression COLON sequence (ELSE COLON sequence)? ;
whileStatement : WHILE expression COLON sequence ;
forStatement : FOR expression IF expressionList COLON sequence ;
returnStatement : RETURN expression NEWLINE ;
printStatement : PRINT expression NEWLINE ;
assignStatement : IDENTIFIER EQUAL expression NEWLINE ;
functionCallStatement : primitiveExpression LEFTPARENT expressionList RIGTHPARENT NEWLINE ;
expressionStatement : expressionList NEWLINE ;
sequence : INDENT moreStatements DEDENT ;
moreStatements : statement+ ;
expression : additionExpression ((LESS|HIGHER| LESSOREQUAL| HIGHEROREQUAL|COMPARISON) additionExpression)* ;
additionExpression : multiplicationExpression ((SUM|SUBTRACTION) multiplicationExpression)* ;
multiplicationExpression : elementExpression ((MULTIPLICATION|DIVISION) elementExpression)* ;
elementExpression : primitiveExpression (LEFTKICK expression RIGTHKICK)* ;
expressionList : expression (COMMA expression)* |  ;
primitiveExpression : NUM | STRING | designator | LEFTPARENT expression RIGTHPARENT | LEFTKICK expressionList RIGTHKICK | LEN LEFTPARENT expression RIGTHPARENT;
designator : IDENTIFIER (LEFTPARENT expressionList RIGTHPARENT)? ;


DEF     : 'def';
LEN     : 'len';
IF      : 'if';
FOR     : 'for';
IN      : 'in';
ELSE    : 'else';
WHILE   : 'while';
RETURN  : 'return';
PRINT   : 'print';
EQUAL   : '=';
COMMA          : ',';
COMPARISON     : '==';
LEFTPARENT     : '(';
RIGTHPARENT    : ')';
SUM            : '+';
MULTIPLICATION    : '*';
DIVISION          : '/';
HIGHER            : '>';
LESS              : '<';
COLON             : ':';
SUBTRACTION       : '-';
LEFTKICK          : '[';
RIGTHKICK         : ']';
LESSOREQUAL       : '<=';
HIGHEROREQUAL     : '>=';

fragment L : [a-zA-Z_];
fragment N : [0-9] ;

CHAR         : '\'' (L|[0-9]|' ')? '\'';
NUM          :'0' | ([1-9] N* ) | ([0-9]+)?(('.'[0-9]+));
IDENTIFIER : L(L|N)*;

STRING : '"' ('""'|~'"')* '"' ;

NEWLINE : ('\r'? '\n' (' ' | '\t')* );

WS : [ +\r\n\t] -> skip ;
BLOK_COMMENT : '"""' .+? ' """ ' ->skip;
COMMENT : '#' ~[\r\n\f]+ ->skip;
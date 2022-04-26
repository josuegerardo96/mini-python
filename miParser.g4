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

program : statement+                                                                         #programAST;

statement: defStatement             #defST
          | ifStatement             #ifST
          | returnStatement         #returnST
          | printStatement          #printST
          | whileStatement          #whileST
          | forStatement            #forST
          | assignStatement         #assignST
          | functionCallStatement   #functionST
          | expressionStatement     #expressionST;

defStatement: DEF IDENTIFIER PIZQ (argList?) PDER DOSPUNT sequence                           #defStatementAST;

argList: IDENTIFIER (COMA IDENTIFIER)*      #argListAST;

moreArgs: (COMA IDENTIFIER)*                #moreArgsAST;

ifStatement: IF expression DOSPUNT sequence (ELSE DOSPUNT sequence)?                         #ifStatementAST;

whileStatement: WHILE expression DOSPUNT sequence                                            #whileStatementAST;

forStatement: FOR expression IN expressionList DOSPUNT sequence                              #forStatementAST;

returnStatement: RETURN expression NEWLINE                                                   #returnStatementAST;

printStatement: PRINT expression NEWLINE                                                     #printStatementAST;

assignStatement: IDENTIFIER ASIGNACION expression NEWLINE                                    #assignStatementAST;

functionCallStatement: primitiveExpression PIZQ expressionList PDER NEWLINE                  #functionCallStatementAST;

expressionStatement: expressionList NEWLINE                                                  #expressionStatementAST;

sequence: INDENT moreStatements DEDENT                                                       #sequenceAST;

moreStatements: statement moreStatements*                                                    #moreStatementsAST;

expression: additionExpression comparison                                                    #expressionAST;

comparison: ((MENOR | MAYOR | MAYORIGUAL | MENORIGUAL | IGUAL)additionExpression)*           #comparisonAST;

additionExpression: multiplicationExpression additionFactor                                  #additionExpressionAST;

additionFactor: ((MAS | MENOS) multiplicationExpression)*                                    #additionFactorAST;

multiplicationExpression: elementExpression multiplicationFactor                             #multiplicationExpressionAST;

multiplicationFactor: (( MULT | DIV ) elementExpression)*                                    #multiplicationFactorAST;

elementExpression: primitiveExpression elementAccess                                         #elementExpressionAST;

elementAccess: (P2IZQ expression P2DER)*                                                     #elementAccessAST;

expressionList: expression moreExpressions                                                   #expressionListAST;

moreExpressions: (COMA expression)*                                                          #moreExpressionsAST;

primitiveExpression: '-'?INTEGER                                                             #integerPrimitiveExpressionAST

                     | '-'?FLOAT                                                             #floatPrimitiveExpressionAST

                     | CHARCONST                                                             #charconstPrimitiveExpressionAST

                     | STRING                                                                #stringPrimitiveExpressionAST

                     | IDENTIFIER (PIZQ expressionList PDER|)                                #identifierPrimitiveExpressionAST

                     | PIZQ expression PDER                                                  #parenthesisPrimitiveExpressionAST

                     | listExpression                                                        #listexpressionPrimitiveExpressionAST

                     | LEN PIZQ expression PDER                                              #lenparenthesisPrimitiveExpressionAST;

listExpression: P2IZQ expressionList P2DER                                                   #listExpressionAST;




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


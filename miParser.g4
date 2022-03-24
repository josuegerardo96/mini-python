grammar miParser;

tokens { INDENT , DEDENT }

program : statement+;

statement: defStatement | ifStatement |returnStatement | printStatement |
whileStatement | forStatement | assignStatement | functionCallStatement |
expressionStatement;

defStatement: DEF IDENTIFIER (argList) DOSPUNT sequence;

argList: IDENTIFIER (COMA IDENTIFIER)*;

moreArgs: (COMA IDENTIFIER)*;

ifStatement: IF expression DOSPUNT sequence ELSE sequence;

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

comparison: ((MENOR | MAYOR | MAYORIGUAL | MENORIGUAL | IGUAL)additionExpression)*;

additionExpression: multiplicationExpression additionFactor;

additionFactor: ((MAS | MENOS) multiplicationExpression)*; 

multiplicationExpression: elementExpression multiplicationFactor;

multiplicationFactor: (PIZQ MULT | DIV PDER elementExpression)*;

elementExpression: primitiveExpression elementAccess;

elementAccess: (P2IZQ expression P2DER)*;

expressionList: expression moreExpressions|;

moreExpressions: (COMA expression)*;

primitiveExpression: INTEGER | FLOAT | CHARCONST | STRING | IDENTIFIER (PIZQ expressionList PDER|)|PIZQ expression
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
CHARCONST : '\'' (SINGLECHARACTER | ESCAPESEQUENCE) '\''; //probar
COMMENTBLOCK : '"""' .*? '"""' ; //probar (adaptado del String)
STRING : '"' .*? '"' ; //probar
SINGCOMMENT: COMMENT;


fragment DIGIT : [0-9];
fragment LETTER : '_'|[a-z];
fragment SINGLECHARACTER:	~['\\\r\n]; //r return / n enter
fragment ESCAPESEQUENCE 	:	'\\' [btnfr"'\\];
fragment COMMENT : '#' ~[\r\n\f]*;



NEWLINE: ('\r'? '\n' (' ' | '\t')*); //For tabs just switch out ' '* with '\t'*

WS  :   [ +\r\n\t] -> skip ;

/**Referencias
http://kedizheng.com/2019/03/31/learning-antlr-4-building-grammar/
https://stackabuse.com/commenting-python-code/
**/
grammar WhileLang;

program: statement+ EOF;

statement: declaration | assignment | whileStatement | ifStatement | breakStatement | continueStatement;

declaration: type ID ASSIGN expr SEMI;

type: INT_TYPE | STRING_TYPE;

assignment: ID ASSIGN expr SEMI;

whileStatement: WHILE LPAREN condition RPAREN LBRACE statement* RBRACE;

ifStatement: IF LPAREN condition RPAREN LBRACE statement* RBRACE (ELSE LBRACE statement* RBRACE)?;

breakStatement: BREAK SEMI;

continueStatement: CONTINUE SEMI;

condition
    : expr                                          # ExprCondition
    | expr (GT | LT | EQ | NE) expr                # ComparisonCondition
    ;

expr
    : ID                                            # idExpr
    | NUMBER                                        # numberExpr
    | STRING                                        # stringExpr
    | expr (PLUS | MINUS | MULT | DIV) expr         # arithmeticExpr
    | LPAREN expr RPAREN                            # parenExpr
    ;

WHILE: 'while';
IF: 'if';
ELSE: 'else';
BREAK: 'break';
CONTINUE: 'continue';
INT_TYPE: 'int';
STRING_TYPE: 'string';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
ASSIGN: '=';
GT: '>';
LT: '<';
EQ: '==';
NE: '!=';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
STRING: '"' (~["\r\n])* '"';
ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
WS: [ \t\r\n]+ -> skip;

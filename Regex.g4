grammar Regex;

regex
    : expression EOF
    ;

expression
    : alternation
    ;

alternation
    : concatenation ('|' right=alternation)?
    ;

concatenation
    : repetition+
    ;

repetition
    : atom q=quantifier?
    ;

quantifier
    : '*'
    | '+'
    | '?'
    ;

atom
    : CHAR
    | '(' expr=expression ')'
    ;

CHAR
    : ~[()*+?| \t\n\r]
    ;

WS
    : [ \t\n\r]+ -> skip
    ;
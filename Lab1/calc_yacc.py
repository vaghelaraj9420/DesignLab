# Yacc example
# source: https://www.dabeaz.com/ply/ply.html#ply_nn4
# to check regular expressions: https://regex101.com/

import ply.yacc as yacc


# Get the token map from the lexer.  This is required.
from calc_lex import tokens

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_mod(p):
    'expression : expression MOD term'
    p[0] = p[1] % p[3]

def p_expression_unaryminus(p):
    'expression : MINUS expression'
    p[0] = -p[2]

def p_expression_pow(p):
    'expression : expression POW term'
    p[0] = p[1] ** p[3]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)


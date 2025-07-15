import ply.yacc as yacc
from lexi import tokens

# I M P O R T A N T E 
# CADA LINEA DEBE TERMINAR CON UN PUNTO Y COMA (;)

# Regla principal: permite varias sentencias separadas
def p_body(p):
    '''body : body sentence
            | sentence'''
    pass

# Una sentencia puede ser un print, una asignación o un comentario
def p_sentence(p):
    '''sentence : PRINT LPAREN print_args RPAREN SEMICOLON
                | ID EQUALS factor SEMICOLON
                | COMMENT'''
    pass

# Argumentos de print: uno o más factores separados por coma
def p_print_args(p):
    '''print_args : print_args COMMA factor
                  | factor'''
    pass

# Un factor puede ser una lista (arreglo)
def p_factor_list(p):
    'factor : LBRACKET elementos RBRACKET'
    pass

# Elementos de la lista: cero, uno o más factores separados por coma
def p_elementos(p):
    '''elementos : elementos COMMA factor
                 | factor
                 | empty'''
    pass

# Un factor puede ser un valor simple
def p_factor_valor(p):
    '''factor : INTEGER
              | FLOAT
              | STR
              | TRUE
              | FALSE
              | ID'''
    pass

# Regla para vacío (lista vacía, argumentos vacíos)
def p_empty(p):
    'empty :'
    pass

# Regla de manejo de errores de sintaxis
def p_error(p):
    print("Error de sintaxis")

# Construir el parser
parser = yacc.yacc()

# Ciclo principal para ingresar código y analizarlo
while True:
    try:
        s = input('sustentación > ')
    except EOFError:
        break
    if not s or s.strip().startswith('#'):
        continue
    result = parser.parse(s)
    if result != None:
        print(result)
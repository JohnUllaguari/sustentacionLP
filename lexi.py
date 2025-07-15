import ply.lex as lex

# I M P O R T A N T E 
# CADA LINEA DEBE TERMINAR CON UN PUNTO Y COMA (;)

#tokensss
tokens = (
    'INTEGER',
    'SEMICOLON',
    'FLOAT',
    'STR',
    'EQUALS',
    'LBRACKET',
    'RBRACKET',
    'LPAREN',
    'RPAREN',
    'COMMA',
    'ID',
    'COMMENT',
)

#reservadas
reserved = {
    'print': 'PRINT',
    'True': 'TRUE',
    'False': 'FALSE'
}

# Agregamos las palabras reservadas
tokens = tokens + tuple(reserved.values())

t_EQUALS = r'='
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'

# A regular expression rule with some action code
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# tambien que reconozca comillas simples 
def t_STR(t):
    r'(\".*?\"|\'.*?\')'
    t.value = t.value[1:-1]
    return t

# Regla para reconocer identificadores y palabras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    if t.type == 'TRUE':
        t.value = True
    elif t.type == 'FALSE':
        t.value = False
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


def t_COMMENT(t):
    r'\#.*'
    pass


# Error handling rule
def t_error(t):
    print("Léxico no válido '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()
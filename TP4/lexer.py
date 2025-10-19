import ply.lex as lex

states = (
    ('moeda', 'exclusive'),
    ('select', 'exclusive')
)

tokens = (
    'LISTAR',
    'INICIO_MOEDA',
    'SELECIONAR',
    'SAIR',
    'EURO',
    'CENT',
    'FIM_MOEDA',
    'VIRG',
    'CODIGO'
)

t_ANY_ignore = '\n\t'

#estado inicial
def t_LISTAR(t):
    r'LISTAR'
    return t

def t_SELECIONAR(t):
    r'SELECIONAR'
    t.lexer.begin('select') #muda para estado select
    return t

def t_INICIO_MOEDA(t):
    r'MOEDA'
    t.lexer.begin('moeda')
    return t

def t_SAIR(t):
    r'SAIR'
    return t

def t_ANY_error(t):
    print (f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

#estado moeda

t_moeda_ignore = ' \t,'

def t_moeda_EURO(t):
    r'\d+e'
    return t

def t_moeda_CENT(t):
    r'\d+c'
    return t

def t_moeda_FIM_MOEDA(t):
    r'\n|\.'
    t.lexer.begin('INITIAL')        #volta ao estado inicial
    return t

def t_moeda_error(t):
    print(f"Carácter ilegal (moeda): {t.value[0]}")
    t.lexer.begin('INITIAL')
    t.lexer.skip(len(t.value))

#estado select
t_select_ignore = ' \t,'
def t_select_CODIGO(t):
    r'[A-Z]\d+'
    t.lexer.begin('INITIAL')
    return t

def t_select_error(t):
    print("maq: Código inválido.")
    t.lexer.begin('INITIAL')
    t.lexer.skip(len(t.value))


#---

lexer = lex.lex()


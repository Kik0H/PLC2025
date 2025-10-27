from lexer import lexer

''' GRAMÁTICA
Expr -> Termo Expr2
Expr2 -> "+" Termo Expr2
       | "-" Termo Expr2
       | Vazio 

Termo -> Fator Termo2
Termo2 -> "*" Fator Termo2
       |  "/" Fator Termo2
       |  Vazio

Fator -> Int 
        | "(" Expr ")"

'''

prox_simb = None

def processa_terminal(tipo):
    global prox_simb
    if tipo == prox_simb.type:
        prox_simb = lexer.token()
    else:
        raise ValueError("Invalid Token")

def rec_Fator():
    global prox_simb
    if prox_simb and prox_simb.type == "INT":
        print (f"Fator -> Int")
        processa_terminal("INT")
    elif prox_simb and prox_simb.type == "PA":
        print (f"Fator -> ( Expr )" )
        processa_terminal("PA")
        rec_Expr()
        if prox_simb and prox_simb.type == "PF":
            processa_terminal("PF")
        else:
            raise ValueError("Falta fechar ')")
    else:
        raise ValueError("Falta INT ou '(")

def rec_Termo2():
    global prox_simb
    if prox_simb and prox_simb.type == "MUL":
        print (f"Termo2 ->  * Fator Termo2")
        processa_terminal("MUL")
        rec_Fator()
        rec_Termo2()
    elif prox_simb and prox_simb.type == "DIV":
        print (f"Termo2 ->  / Fator Termo2")
        processa_terminal("DIV")
        rec_Fator()
        rec_Termo2()
    else:
        print (f"Vazio")
        pass

def rec_Termo():
    print (f"Termo -> Fator Termo2")
    rec_Fator()
    rec_Termo2()

def rec_Expr2():
    global prox_simb
    if prox_simb and prox_simb.type == "SUM":
        print (f"Expr2 ->  + Termo Expr2")
        processa_terminal("SUM")
        rec_Termo()
        rec_Expr2()
    elif prox_simb and prox_simb.type == "SUB":
        print (f"Expr2 ->  - Termo Expr2")
        processa_terminal("SUB")
        rec_Termo()
        rec_Expr2()
    else:
        print (f"Vazio")
        pass

def rec_Expr():
    print (f"Expr ->  Termo Expr2")
    rec_Termo()
    rec_Expr2()

def rec_Parser(l):
    global prox_simb
    lexer.input(l)
    prox_simb = lexer.token()
    rec_Expr()
    if prox_simb is not None:
        raise ValueError (f"Valor inesperado no input: {prox_simb.value}")
    print("ACABOU!")

l = input("Introduza uma expressão: ")
rec_Parser(l)
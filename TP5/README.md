# TP5 

Neste trabalho prático foi proposto construir um parser (recursivo descendente) para expressões com símbolos aritméticos e parênteses.

Foi preciso construir uma gramática que reconhecesse o tipo das expressões pretendidas, bem como o analisador léxico.

## Gramática adotada
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

## Ficheiros
[Lexer](lexer.py)

[Parser](parser.py)

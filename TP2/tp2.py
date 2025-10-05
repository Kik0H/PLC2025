import re

def md_para_html(texto):
    linhas = texto.splitlines()     #Para tratar linha a linha
    resultado = []
    ol = False      #Assim consigo abrir e fechar o <ol> nas listas numeradas
    
    for linha in linhas:
        #LISTAS
        if re.match(r"\d+\. (.*)", linha):
            if not ol:
                resultado.append("<ol>")
                ol = True          #Lista aberta
            resultado.append(re.sub(r"^\d+\. (.*)", r"<li>\1</li>", linha))
            continue

        if ol:      #Se a linha não for um item de uma lista, mas a flag ainda for true, temos de fechar a lista primeiro
            resultado.append("</ol>")
            ol = False  

        #CABECALHOS
        if re.match(r"^### (.*)", linha):
            resultado.append(re.sub(r"^### (.*)", r"<h3>\1</h3>", linha))   #Grupo de captura (Tudo o que está depois do ###, fica entre <h3></h3>)
            continue
        if re.match(r"^## (.*)", linha):
            resultado.append(re.sub(r"^## (.*)", r"<h2>\1</h2>", linha))
            continue
        if re.match(r"^# (.*)", linha):
            resultado.append(re.sub(r"^# (.*)", r"<h1>\1</h1>", linha))
            continue

        resultado.append(linha)     #Casos normais + BOLD + ITALICO + LINKS + IMAGENS
        
    if ol:
        resultado.append("</ol>")   #Se tiver uma lista no fim do texto
    
    
    html = ("\n".join(resultado))   #Transforma a lista em string
        
    #Como os restantes casos podem aparecer em qualquer posição numa linha, posso substituir fora do loop
    #Com os cabeçalhos e as listas MUDAM uma linha inteira (por não terem um "limite" na expressão regular para fechar), é mais fácil analizar linha a linha e tratar destes casos no loop

    #Uso o operador ? para tornar o operador * lazy.
    #Se não, em casos onde tenha 2 BOLDS ou 1 BOLD e 1 itálico na mesma linha, vai ficar mal feito, porque o operador * lê mais do que precisa

    #BOLD 
    html = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", html)

    #ITALICO
    html = re.sub(r"\*(.*?)\*", r"<i>\1</i>", html)

    #IMAGENS (tem que ser tratadas primeiro do que os LINKS, para não causar problemas)
    html = re.sub(r"!\[(.*?)\]\((.*?)\)", r'<img src="\2" alt="\1"/>', html)

    #LINKS
    html = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', html)

    return html


md = """# Exemplo
## Teste 2
### Teste 3
Este é um **exemplo** e este é um *teste*.
1. Primeiro item
2. Segundo item
3. Terceiro item
Como pode ser consultado em [página da UC](http://www.uc.pt) 
Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...
"""
print(md_para_html(md))
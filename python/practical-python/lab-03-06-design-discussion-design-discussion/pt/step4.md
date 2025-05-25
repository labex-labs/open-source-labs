# Exercício 3.17: De nomes de arquivos para objetos semelhantes a arquivos

Você agora criou um arquivo `fileparse.py` que contém uma função `parse_csv()`. A função funcionava assim:

```python
>>> import fileparse
>>> portfolio = fileparse.parse_csv('portfolio.csv', types=[str,int,float])
>>>
```

No momento, a função espera receber um nome de arquivo. No entanto, você pode tornar o código mais flexível. Modifique a função para que ela funcione com qualquer objeto semelhante a arquivo/iterável. Por exemplo:

```python
>>> import fileparse
>>> import gzip
>>> with gzip.open('portfolio.csv.gz', 'rt') as file:
...      port = fileparse.parse_csv(file, types=[str,int,float])
...
>>> lines = ['name,shares,price', 'AA,100,34.23', 'IBM,50,91.1', 'HPE,75,45.1']
>>> port = fileparse.parse_csv(lines, types=[str,int,float])
>>>
```

Neste novo código, o que acontece se você passar um nome de arquivo como antes?

```python
>>> port = fileparse.parse_csv('portfolio.csv', types=[str,int,float])
>>> port
... look at output (it should be crazy) ...
>>>
```

Sim, você precisará ter cuidado. Você poderia adicionar uma verificação de segurança para evitar isso?

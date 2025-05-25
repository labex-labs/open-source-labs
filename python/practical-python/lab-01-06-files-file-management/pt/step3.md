# Idiomas Comuns para Escrever em um Arquivo

Escrever dados de string.

```python
with open('outfile', 'wt') as out:
    out.write('Hello World\n')
    ...
```

Redirecionar a função print.

```python
with open('outfile', 'wt') as out:
    print('Hello World', file=out)
    ...
```

Estes exercícios dependem de um arquivo `portfolio.csv`. O arquivo contém uma lista de linhas com informações sobre uma carteira de ações. Assume-se que você está trabalhando no diretório `~/project/`. Se você não tiver certeza, pode descobrir onde o Python acha que está executando fazendo o seguinte:

```python
>>> import os
>>> os.getcwd()
'/home/labex/project' # Output vary
>>>
```

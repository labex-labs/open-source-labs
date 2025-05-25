# Exercício 3.11: Importações de Módulos

Na seção 3, criamos uma função de uso geral `parse_csv()` para analisar o conteúdo de arquivos de dados CSV.

Agora, vamos ver como usar essa função em outros programas. Primeiro, inicie em uma nova janela do shell. Navegue até a pasta onde você tem todos os seus arquivos. Vamos importá-los.

Inicie o modo interativo do Python.

```shell
$ python3
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Depois de fazer isso, tente importar alguns dos programas que você escreveu anteriormente. Você deve ver a saída deles exatamente como antes. Só para enfatizar, importar um módulo executa seu código.

```python
>>> import bounce
... watch output ...
>>> import mortgage
... watch output ...
>>> import report
... watch output ...
>>>
```

Se nada disso funcionar, você provavelmente está executando o Python no diretório errado. Agora, tente importar seu módulo `fileparse` e obter alguma ajuda sobre ele.

```python
>>> import fileparse
>>> help(fileparse)
... look at the output ...
>>> dir(fileparse)
... look at the output ...
>>>
```

Tente usar o módulo para ler alguns dados:

```python
>>> portfolio = fileparse.parse_csv('/home/labex/project/portfolio.csv',select=['name','shares','price'], types=[str,int,float])
>>> portfolio
... look at the output ...
>>> pricelist = fileparse.parse_csv('/home/labex/project/prices.csv',types=[str,float], has_headers=False)
>>> pricelist
... look at the output ...
>>> prices = dict(pricelist)
>>> prices
... look at the output ...
>>> prices['IBM']
106.28
>>>
```

Tente importar uma função para que você não precise incluir o nome do módulo:

```python
>>> from fileparse import parse_csv
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv', select=['name','shares','price'], types=[str,int,float])
>>> portfolio
... look at the output ...
>>>
```

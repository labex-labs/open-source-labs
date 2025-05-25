# Exercício 6.4: Um Gerador Simples

Se você se encontrar querendo personalizar a iteração, você sempre deve pensar em funções geradoras (generator functions). Elas são fáceis de escrever---crie uma função que execute a lógica de iteração desejada e use `yield` para emitir valores.

Por exemplo, experimente este gerador que pesquisa um arquivo por linhas contendo uma substring correspondente:

```python
>>> def filematch(filename, substr):
        with open(filename, 'r') as f:
            for line in f:
                if substr in line:
                    yield line

>>> for line in open('portfolio.csv'):
        print(line, end='')

name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>> for line in filematch('portfolio.csv', 'IBM'):
        print(line, end='')

"IBM",50,91.10
"IBM",100,70.44
>>>
```

Isso é interessante---a ideia de que você pode esconder um monte de processamento personalizado em uma função e usá-la para alimentar um loop for. O próximo exemplo analisa um caso mais incomum.

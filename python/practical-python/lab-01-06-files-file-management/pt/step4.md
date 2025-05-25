# Exercício 1.26: Preliminares de Arquivos

Primeiro, tente ler o arquivo inteiro de uma vez como uma grande string:

```python
>>> with open('portfolio.csv', 'rt') as f:
        data = f.read()

>>> data
'name,shares,price\n"AA",100,32.20\n"IBM",50,91.10\n"CAT",150,83.44\n"MSFT",200,51.23\n"GE",95,40.37\n"MSFT",50,65.10\n"IBM",100,70.44\n'
>>> print(data)
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>>
```

No exemplo acima, deve-se notar que o Python tem dois modos de saída. No primeiro modo, onde você digita `data` no prompt, o Python mostra a representação da string bruta, incluindo aspas e códigos de escape. Quando você digita `print(data)`, você obtém a saída formatada real da string.

Embora ler um arquivo de uma vez seja simples, muitas vezes não é a maneira mais apropriada de fazê-lo - especialmente se o arquivo for enorme ou se contiver linhas de texto que você deseja manipular uma de cada vez.

Para ler um arquivo linha por linha, use um loop for como este:

```python
>>> with open('portfolio.csv', 'rt') as f:
        for line in f:
            print(line, end='')

name,shares,price
"AA",100,32.20
"IBM",50,91.10
...
>>>
```

Quando você usa este código como mostrado, as linhas são lidas até que o final do arquivo seja alcançado, momento em que o loop para.

Em certas ocasiões, você pode querer ler ou pular manualmente uma _única_ linha de texto (por exemplo, talvez você queira pular a primeira linha de cabeçalhos de coluna).

```python
>>> f = open('portfolio.csv', 'rt')
>>> headers = next(f)
>>> headers
'name,shares,price\n'
>>> for line in f:
    print(line, end='')

"AA",100,32.20
"IBM",50,91.10
...
>>> f.close()
>>>
```

`next()` retorna a próxima linha de texto no arquivo. Se você o chamasse repetidamente, obteria linhas sucessivas. No entanto, para que você saiba, o loop `for` já usa `next()` para obter seus dados. Assim, você normalmente não o chamaria diretamente, a menos que esteja tentando explicitamente pular ou ler uma única linha, como mostrado.

Depois de ler as linhas de um arquivo, você pode começar a realizar mais processamento, como divisão (splitting). Por exemplo, tente isto:

```python
>>> f = open('portfolio.csv', 'rt')
>>> headers = next(f).split(',')
>>> headers
['name', 'shares', 'price\n']
>>> for line in f:
    row = line.split(',')
    print(row)

['"AA"', '100', '32.20\n']
['"IBM"', '50', '91.10\n']
...
>>> f.close()
```

_Nota: Nestes exemplos, `f.close()` está sendo chamado explicitamente porque a instrução `with` não está sendo usada._

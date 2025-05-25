# Exercício 2.11: Adicionando alguns cabeçalhos

Suponha que você tenha uma tupla de nomes de cabeçalho como esta:

```python
headers = ('Name', 'Shares', 'Price', 'Change')
```

Adicione código ao seu programa que pegue a tupla de cabeçalhos acima e crie uma string onde cada nome de cabeçalho seja alinhado à direita em um campo de 10 caracteres de largura e cada campo seja separado por um único espaço.

```python
'      Name     Shares      Price      Change'
```

Escreva código que pegue os cabeçalhos e crie a string separadora entre os cabeçalhos e os dados a seguir. Esta string é apenas um monte de caracteres "-" sob cada nome de campo. Por exemplo:

```python
'---------- ---------- ---------- -----------'
```

Quando terminar, seu programa deverá produzir a tabela mostrada no início deste exercício.

          Name     Shares      Price     Change
    ---------- ---------- ---------- ----------
            AA        100       9.22     -22.98
           IBM         50     106.28      15.18
           CAT        150      35.46     -47.98
          MSFT        200      20.89     -30.34
            GE         95      13.48     -26.89
          MSFT         50      20.89     -44.21
           IBM        100     106.28      35.84

# Função zip()

A função `zip` recebe múltiplas sequências e cria um iterador que as combina.

```python
columns = ['name', 'shares', 'price']
values = ['GOOG', 100, 490.1 ]
pairs = zip(columns, values)
# ('name','GOOG'), ('shares',100), ('price',490.1)
```

Para obter o resultado, você deve iterar. Você pode usar múltiplas variáveis para desempacotar as tuplas, como mostrado anteriormente.

```python
for column, value in pairs:
    ...
```

Um uso comum de `zip` é criar pares chave/valor para construir dicionários.

```python
d = dict(zip(columns, values))
```

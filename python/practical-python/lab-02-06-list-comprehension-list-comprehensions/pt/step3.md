# Casos de uso

List comprehensions (compreensões de lista) são extremamente úteis. Por exemplo, você pode coletar valores de campos específicos de um dicionário:

```python
stocknames = [s['name'] for s in stocks]
```

Você pode realizar consultas semelhantes a bancos de dados em sequências.

```python
a = [s for s in stocks if s['price'] > 100 and s['shares'] > 50 ]
```

Você também pode combinar uma list comprehension (compreensão de lista) com uma redução de sequência:

```python
cost = sum([s['shares']*s['price'] for s in stocks])
```

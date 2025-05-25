# Acesso Uniforme

O último exemplo mostra como colocar uma interface mais uniforme em um objeto. Se você não fizer isso, um objeto pode ser confuso de usar:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> a = s.cost() # Method
49010.0
>>> b = s.shares # Data attribute
100
>>>
```

Por que os `()` são necessários para o custo, mas não para as ações (shares)? Uma propriedade pode corrigir isso.

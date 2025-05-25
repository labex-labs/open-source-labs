# Dicionários (Dicts) como um Contêiner (Container)

Dicionários são úteis se você deseja pesquisas aleatórias rápidas (por nome da chave). Por exemplo, um dicionário de preços de ações:

```python
prices = {
   'GOOG': 513.25,
   'CAT': 87.22,
   'IBM': 93.37,
   'MSFT': 44.12
}
```

Aqui estão algumas pesquisas simples:

```python
>>> prices['IBM']
93.37
>>> prices['GOOG']
513.25
>>>
```

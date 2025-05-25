# Lambda: Funções Anônimas

Use uma lambda em vez de criar a função. Em nosso exemplo de ordenação anterior.

```python
portfolio.sort(key=lambda s: s['name'])
```

Isso cria uma função _sem nome_ que avalia uma _única_ expressão. O código acima é muito mais curto do que o código inicial.

```python
def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name)

# vs lambda
portfolio.sort(key=lambda s: s['name'])
```

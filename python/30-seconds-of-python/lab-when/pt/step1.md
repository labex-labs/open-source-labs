# Aplicar Função Quando Verdadeiro

Escreva uma função chamada `when` que recebe dois argumentos: uma função predicado `predicate` e uma função a ser aplicada `when_true`. A função `when` deve retornar uma nova função que recebe um único argumento `x`. A nova função deve verificar se o valor de `predicate(x)` é `True`. Se for, a nova função deve chamar `when_true(x)` e retornar o resultado. Caso contrário, a nova função deve retornar `x`.

```python
def when(predicate, when_true):
  return lambda x: when_true(x) if predicate(x) else x
```

```python
double_even_numbers = when(lambda x: x % 2 == 0, lambda x : x * 2)
double_even_numbers(2) # 4
double_even_numbers(1) # 1
```

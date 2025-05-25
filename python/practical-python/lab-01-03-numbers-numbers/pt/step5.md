# Comparações (Comparisons)

Os seguintes operadores de comparação/relacionais funcionam com números:

    x < y      Menor que (Less than)
    x <= y     Menor ou igual a (Less than or equal)
    x > y      Maior que (Greater than)
    x >= y     Maior ou igual a (Greater than or equal)
    x == y     Igual a (Equal to)
    x != y     Diferente de (Not equal to)

Você pode formar expressões booleanas mais complexas usando

`and`, `or`, `not`

Aqui estão alguns exemplos:

```python
if b >= a and b <= c:
    print('b is between a and c')

if not (b < a or b > c):
    print('b is still between a and c')
```

# Comparaciones

Los siguientes operadores de comparación / relacionales funcionan con números:

    x < y      Menor que
    x <= y     Menor o igual que
    x > y      Mayor que
    x >= y     Mayor o igual que
    x == y     Igual a
    x!= y     Diferente de

Puede formar expresiones booleanas más complejas utilizando

`and`, `or`, `not`

Aquí hay algunos ejemplos:

```python
if b >= a and b <= c:
    print('b está entre a y c')

if not (b < a or b > c):
    print('b todavía está entre a y c')
```

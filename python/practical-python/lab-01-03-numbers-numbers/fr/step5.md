# Comparaisons

Les opérateurs de comparaison / relationnels suivants fonctionnent avec les nombres :

    x < y      Moins que
    x <= y     Moins ou égal à
    x > y      Plus que
    x >= y     Plus ou égal à
    x == y     Égal à
    x!= y     Différent de

Vous pouvez former des expressions booléennes plus complexes en utilisant

`et`, `ou`, `non`

Voici quelques exemples :

```python
if b >= a et b <= c:
    print('b est compris entre a et c')

if non (b < a ou b > c):
    print('b est toujours compris entre a et c')
```

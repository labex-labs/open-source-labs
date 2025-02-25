# Factoriel

Écrivez une fonction `factorial(num)` qui prend un entier non négatif `num` en argument et renvoie son factoriel. La fonction doit utiliser la récursion pour calculer le factoriel. Si `num` est inférieur ou égal à `1`, renvoyez `1`. Sinon, renvoyez le produit de `num` et du factoriel de `num - 1`. La fonction doit lever une exception si `num` est un nombre négatif ou un nombre à virgule flottante.

```python
def factorial(num):
  if not ((num >= 0) and (num % 1 == 0)):
    raise Exception("Number can't be floating point or negative.")
  return 1 if num == 0 else num * factorial(num - 1)
```

```python
factorial(6) # 720
```

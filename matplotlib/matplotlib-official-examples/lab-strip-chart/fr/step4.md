# Création de la fonction émettrice

La fonction émettrice génère les données qui seront transmises à la méthode de mise à jour. Dans ce cas, nous générons des données aléatoires avec une probabilité de 0,1.

```python
def emitter(p=0.1):
    while True:
        v = np.random.rand()
        if v > p:
            yield 0.
        else:
            yield np.random.rand()
```

# Créer des points de données

Dans cette étape, nous allons créer quelques points de données à l'aide de la classe d'unité personnalisée - `Foo`.

```python
# créer quelques Foos
x = [Foo(val, 1.0) for val in range(0, 50, 2)]
# et quelques données y arbitraires
y = [i for i in range(len(x))]
```

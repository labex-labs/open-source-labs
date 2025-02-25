# Créez des données pour le tracé

Ensuite, créons quelques données que nous utiliserons pour tracer. Nous utiliserons la fonction `numpy.arange()` pour créer un tableau de valeurs de 0 à 14 et le stocker dans la variable `x`. Nous utiliserons également la fonction `numpy.sin()` pour créer un tableau de valeurs qui sont le sinus de chaque valeur de `x` divisée par 2, et le stocker dans la variable `y`.

```python
x = np.arange(14)
y = np.sin(x / 2)
```

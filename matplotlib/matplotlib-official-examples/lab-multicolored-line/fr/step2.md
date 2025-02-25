# Création des données

Nous allons créer un tableau numpy `x` contenant 500 valeurs régulièrement espacées entre 0 et 3π. Nous allons également créer un autre tableau numpy `y` contenant le sinus des valeurs de `x`. Enfin, nous allons créer un tableau numpy `dydx` contenant la première dérivée de `y`.

```python
x = np.linspace(0, 3 * np.pi, 500)
y = np.sin(x)
dydx = np.cos(0.5 * (x[:-1] + x[1:]))
```

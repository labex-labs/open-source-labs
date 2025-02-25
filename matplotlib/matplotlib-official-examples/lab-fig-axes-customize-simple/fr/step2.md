# Création d'une figure et définition de l'arrière-plan

Nous allons créer une figure à l'aide de la méthode `plt.figure()`, qui crée une instance `matplotlib.figure.Figure`. Nous allons définir la couleur d'arrière-plan de la figure à l'aide de la méthode `rect.set_facecolor()`.

```python
fig = plt.figure()
rect = fig.patch  # une instance de rectangle
rect.set_facecolor('lightgoldenrodyellow')
```

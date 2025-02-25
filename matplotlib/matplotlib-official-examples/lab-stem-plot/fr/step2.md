# Générer des données

Ensuite, nous devons générer des données à utiliser dans notre diagramme en tiges. Nous allons créer deux tableaux à l'aide de la bibliothèque Numpy.

```python
x = np.linspace(0.1, 2 * np.pi, 41)
y = np.exp(np.sin(x))
```

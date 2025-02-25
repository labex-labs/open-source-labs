# Générer des données

Dans cette étape, nous allons générer les données pour le graphique en ligne. Nous utiliserons la fonction `arange()` de NumPy pour générer un tableau de valeurs pour l'axe des x, et la fonction `sin()` pour générer un tableau de valeurs pour l'axe des y pour une onde sinusoïdale.

```python
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))
```

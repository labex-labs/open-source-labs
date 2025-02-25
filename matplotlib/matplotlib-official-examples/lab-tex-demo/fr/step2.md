# Créer un graphique en ligne simple

Dans cette étape, nous allons créer un graphique en ligne simple à l'aide de Matplotlib. Nous commencerons par générer des données à représenter à l'aide des fonctions `linspace()` et `cos()` de NumPy. Ensuite, nous utiliserons la fonction `plot()` pour créer le graphique.

```python
t = np.linspace(0.0, 1.0, 100)
s = np.cos(4 * np.pi * t) + 2

plt.plot(t, s)
plt.show()
```

# Créer un diagramme de dispersion

Dans cette étape, nous allons créer un diagramme de dispersion à l'aide de Matplotlib. Nous commencerons par générer des données aléatoires à représenter à l'aide de la fonction `random()` de NumPy. Ensuite, nous utiliserons la fonction `scatter()` pour créer le diagramme.

```python
x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y)
plt.show()
```

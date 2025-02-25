# Créer un graphique en barres

Dans cette étape, nous allons créer un graphique en barres à l'aide de Matplotlib. Nous commencerons par générer des données à représenter à l'aide de la fonction `random()` de NumPy. Ensuite, nous utiliserons la fonction `bar()` pour créer le graphique.

```python
x = ['A', 'B', 'C', 'D', 'E']
y = np.random.randint(1, 10, 5)

plt.bar(x, y)
plt.show()
```

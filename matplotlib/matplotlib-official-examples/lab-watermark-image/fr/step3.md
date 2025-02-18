# Créer un graphique

Maintenant, nous pouvons créer le graphique sur lequel nous souhaitons superposer l'image. Dans cet exemple, nous allons créer un simple graphique à barres en utilisant des données aléatoires.

```python
fig, ax = plt.subplots()

np.random.seed(19680801)
x = np.arange(30)
y = x + np.random.randn(30)
ax.bar(x, y, color='#6bbc6b')
ax.grid()
```

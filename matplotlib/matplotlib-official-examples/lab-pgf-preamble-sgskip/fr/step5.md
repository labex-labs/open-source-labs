# Créer un graphique en nuage de points

En plus des graphiques linéaires, Matplotlib peut également créer des graphiques en nuage de points. Voici un exemple :

```python
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 500 * np.random.rand(50)

plt.scatter(x, y, c=colors, s=sizes)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphique en nuage de points')
plt.show()
```

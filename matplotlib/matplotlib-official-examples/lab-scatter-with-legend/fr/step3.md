# Création automatique de légende

Nous pouvons également utiliser la méthode `PathCollection.legend_elements` pour créer automatiquement une légende pour un graphique à points de dispersion. Cette méthode tentera de déterminer un nombre utile d'entrées de légende à afficher et renverra un tuple de poignées et d'étiquettes.

```python
N = 45
x, y = np.random.rand(2, N)
c = np.random.randint(1, 5, size=N)
s = np.random.randint(10, 220, size=N)

fig, ax = plt.subplots()

scatter = ax.scatter(x, y, c=c, s=s)

# produire une légende avec les couleurs uniques du graphique à points de dispersion
legend1 = ax.legend(*scatter.legend_elements(),
                    loc="lower left", title="Classes")
ax.add_artist(legend1)

# produire une légende avec une tranche d'échelles du graphique à points de dispersion
handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
legend2 = ax.legend(handles, labels, loc="upper right", title="Sizes")

plt.show()
```

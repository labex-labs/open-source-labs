# Personnalisation des éléments de la légende

Nous pouvons personnaliser davantage les éléments de la légende en utilisant des arguments supplémentaires dans la méthode `PathCollection.legend_elements`. Par exemple, nous pouvons spécifier le nombre d'entrées de légende à créer et comment elles devraient être étiquetées.

```python
volume = np.random.rayleigh(27, size=40)
amount = np.random.poisson(10, size=40)
ranking = np.random.normal(size=40)
price = np.random.uniform(1, 10, size=40)

fig, ax = plt.subplots()

# Étant donné que le prix est beaucoup trop petit lorsqu'il est utilisé comme taille pour ``s``,
# nous le normalisons à des tailles de points utiles, s=0.3*(prix*3)**2
scatter = ax.scatter(volume, amount, c=ranking, s=0.3*(price*3)**2,
                     vmin=-3, vmax=3, cmap="Spectral")

# Créer une légende pour le classement (couleurs). Même s'il y a 40 classements différents,
# nous ne voulons montrer que 5 d'entre eux dans la légende.
legend1 = ax.legend(*scatter.legend_elements(num=5),
                    loc="upper left", title="Ranking")
ax.add_artist(legend1)

# Créer une légende pour le prix (tailles). Étant donné que nous voulons montrer les prix
# en dollars, nous utilisons l'argument *func* pour fournir l'inverse de la fonction
# utilisée pour calculer les tailles ci-dessus. Le *fmt* assure d'afficher le prix
# en dollars. Notez comment nous visons 5 éléments ici, mais obtenons seulement 4 dans la
# légende créée en raison des prix arrondis automatiques qui sont choisis pour nous.
kw = dict(prop="sizes", num=5, color=scatter.cmap(0.7), fmt="$ {x:.2f}",
          func=lambda s: np.sqrt(s/.3)/3)
legend2 = ax.legend(*scatter.legend_elements(**kw),
                    loc="lower right", title="Price")

plt.show()
```

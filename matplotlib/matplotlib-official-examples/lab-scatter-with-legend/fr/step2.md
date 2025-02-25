# Création d'un graphique à points de dispersion avec plusieurs groupes

Nous pouvons créer un graphique à points de dispersion avec plusieurs groupes en parcourant chaque groupe et en créant un graphique à points de dispersion pour ce groupe. Nous spécifions la couleur, la taille et la transparence des marqueurs pour chaque groupe en utilisant respectivement les paramètres `c`, `s` et `alpha`. Nous définissons également le paramètre `label` sur le nom du groupe, qui sera utilisé dans la légende.

```python
fig, ax = plt.subplots()
for color in ['tab:blue', 'tab:orange', 'tab:green']:
    n = 750
    x, y = np.random.rand(2, n)
    scale = 200.0 * np.random.rand(n)
    ax.scatter(x, y, c=color, s=scale, label=color,
               alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)

plt.show()
```

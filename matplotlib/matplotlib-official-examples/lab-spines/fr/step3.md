# Créer des sous-graphiques

Nous allons créer trois sous-graphiques pour démontrer différentes personnalisations des épines. Nous utiliserons un agencement contraint pour vous assurer que les étiquettes ne chevauchent pas les axes.

```python
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, layout='constrained')
```

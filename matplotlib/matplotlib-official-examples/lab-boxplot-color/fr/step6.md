# Ajout de lignes de grille horizontales

Enfin, nous allons ajouter des lignes de grille horizontales aux diagrammes en boîte à l'aide de la fonction `yaxis.grid()`.

```python
for ax in [ax1, ax2]:
    ax.yaxis.grid(True)
    ax.set_xlabel('Trois échantillons séparés')
    ax.set_ylabel('Valeurs observées')

plt.show()
```

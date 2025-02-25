# Etiquetez la figure

Dans cette étape, nous allons étiqueter la figure. Nous allons ajouter un titre, des lignes de grille et des étiquettes pour les axes x et y.

```python
fig.suptitle("Cumulative Distributions")
for ax in axs:
    ax.grid(True)
    ax.legend()
    ax.set_xlabel("Annual rainfall (mm)")
    ax.set_ylabel("Probability of occurrence")
    ax.label_outer()

plt.show()
```

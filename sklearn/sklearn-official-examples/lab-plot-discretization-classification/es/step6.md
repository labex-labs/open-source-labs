# Visualizar los resultados

En este paso, visualizaremos los resultados del proceso de discretización de características. Graficaremos la precisión de clasificación en el conjunto de prueba para cada clasificador y conjunto de datos.

```python
plt.tight_layout()

# Add suptitles above the figure
plt.subplots_adjust(top=0.90)
suptitles = [
    "Linear classifiers",
    "Feature discretization and linear classifiers",
    "Non-linear classifiers",
]
for i, suptitle in zip([1, 3, 5], suptitles):
    ax = axes[0, i]
    ax.text(
        1.05,
        1.25,
        suptitle,
        transform=ax.transAxes,
        horizontalalignment="center",
        size="x-large",
    )
plt.show()
```

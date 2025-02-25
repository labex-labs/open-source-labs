# Personnalisez l'histogramme

Dans cette étape, nous allons personnaliser l'histogramme en ajoutant des étiquettes, un titre et en ajustant la mise en page.

```python
ax.set_xlabel('Smarts')
ax.set_ylabel('Probabilité de densité')
ax.set_title(r'Histogramme de l'IQ : $\mu=100$, $\sigma=15$')
fig.tight_layout()
plt.show()
```

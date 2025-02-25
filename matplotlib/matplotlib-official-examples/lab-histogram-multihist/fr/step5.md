# Personnalisez l'histogramme

Nous pouvons personnaliser l'histogramme en changeant la couleur, la transparence et la couleur des bords des barres en utilisant les paramètres `color`, `alpha` et `edgecolor`.

```python
plt.hist(x, n_bins, color='green', alpha=0.5, edgecolor='black')
plt.xlabel('Valeur')
plt.ylabel('Fréquence')
plt.title('Histogramme de données aléatoires')
plt.show()
```

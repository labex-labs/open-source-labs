# Tracez plusieurs histogrammes

Nous pouvons tracer plusieurs histogrammes sur le même graphique en passant un tableau de données à la fonction `hist`.

```python
plt.hist(x, n_bins, color='green', alpha=0.5, edgecolor='black', label=['Sample 1', 'Sample 2', 'Sample 3'])
plt.xlabel('Valeur')
plt.ylabel('Fréquence')
plt.title('Histogramme de données aléatoires')
plt.legend()
plt.show()
```

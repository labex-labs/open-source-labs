# Tracez des histogrammes superposés

Nous pouvons tracer des histogrammes superposés en définissant le paramètre `stacked` sur `True`.

```python
plt.hist(x, n_bins, color=['green', 'blue','red'], alpha=0.5, edgecolor='black', label=['Sample 1', 'Sample 2', 'Sample 3'], stacked=True)
plt.xlabel('Valeur')
plt.ylabel('Fréquence')
plt.title('Histogramme superposé de données aléatoires')
plt.legend()
plt.show()
```

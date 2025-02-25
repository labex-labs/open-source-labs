# Tracez des histogrammes en escalier

Nous pouvons tracer des histogrammes en escalier en définissant le paramètre `histtype` sur `'step'`.

```python
plt.hist(x, n_bins, histtype='step', color=['green', 'blue','red'], label=['Sample 1', 'Sample 2', 'Sample 3'])
plt.xlabel('Valeur')
plt.ylabel('Fréquence')
plt.title('Histogramme en escalier de données aléatoires')
plt.legend()
plt.show()
```

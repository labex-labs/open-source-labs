# Zeichnen mehrerer Histogramme

Wir können mehrere Histogramme auf dem gleichen Diagramm zeichnen, indem wir einem Array von Daten an die `hist`-Funktion übergeben.

```python
plt.hist(x, n_bins, color='green', alpha=0.5, edgecolor='black', label=['Sample 1', 'Sample 2', 'Sample 3'])
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.legend()
plt.show()
```

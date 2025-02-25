# Anpassen des Histogramms

Wir können das Histogramm anpassen, indem wir die Farbe, die Transparenz und die Kantenfarbe der Balken mit den Parametern `color`, `alpha` und `edgecolor` ändern.

```python
plt.hist(x, n_bins, color='green', alpha=0.5, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.show()
```

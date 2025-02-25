# Rendern des Barcodes

Schließlich können wir den Barcode mit `Axes.imshow` rendern. Wir werden `code.reshape(1, -1)` verwenden, um die Daten in ein 2D-Array mit einer Zeile umzuwandeln, `imshow(..., aspect='auto')`, um nicht quadratische Pixel zuzulassen, und `imshow(..., interpolation='nearest')`, um verschwommene Kanten zu vermeiden.

```python
ax.imshow(code.reshape(1, -1), cmap='binary', aspect='auto',
          interpolation='nearest')
plt.show()
```

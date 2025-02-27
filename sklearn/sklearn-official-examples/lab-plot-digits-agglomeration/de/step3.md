# Verbindungsmatrix definieren

In diesem Schritt werden wir die Verbindungsmatrix mit der Funktion `grid_to_graph` aus scikit-learn definieren. Diese Funktion erstellt einen Verbindungsgraphen basierend auf dem Pixelgitter der Bilder.

```python
connectivity = grid_to_graph(*images[0].shape)
```

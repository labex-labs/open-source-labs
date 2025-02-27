# Den Datensatz vorbereiten

Wir müssen die Bilder flach drehen, um jedes 2D-Array von Graustufenwerten von der Form `(8, 8)` in die Form `(64,)` zu bringen. Dies wird uns einen Datensatz der Form `(n_samples, n_features)` geben, wobei `n_samples` die Anzahl der Bilder und `n_features` die Gesamtzahl der Pixel in jedem Bild ist.

```python
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))
```

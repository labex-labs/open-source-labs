# Generieren der Ecken der Rechtecke

Um unser Histogramm mit Rechtecken zu zeichnen, müssen wir die Ecken jedes Rechtecks berechnen. Fügen Sie den folgenden Code hinzu:

```python
left = bins[:-1]
right = bins[1:]
bottom = np.zeros(len(left))
top = bottom + n
```

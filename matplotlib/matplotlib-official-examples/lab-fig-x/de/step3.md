# Fügen von Linien zur Figur hinzu

Wir können Linien zur Figur hinzufügen, indem wir die `fig.add_artist()`-Methode verwenden. Wir werden zwei Linien erstellen - eine von (0,0) nach (1,1) und eine andere von (0,1) nach (1,0).

```python
fig.add_artist(lines.Line2D([0, 1], [0, 1]))
fig.add_artist(lines.Line2D([0, 1], [1, 0]))
```

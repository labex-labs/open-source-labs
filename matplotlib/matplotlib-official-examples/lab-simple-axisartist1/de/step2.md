# Figur und Teilplots erstellen

Wir werden eine Figur mit zwei Teilplots mit der Methode `add_gridspec` erstellen.

```python
fig = plt.figure(figsize=(6, 3), layout="constrained")
gs = fig.add_gridspec(1, 2)
```

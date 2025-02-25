# Erstellen einer Figur und zweier Teilplots

Wir werden mithilfe der Methode `subplots()` eine Figur mit zwei Teilplots erstellen. Wir werden auch die Projektion auf `'3d'` einstellen, sodass unsere Teilplots dreidimensional sind.

```python
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(8, 12), subplot_kw={'projection': '3d'})
```

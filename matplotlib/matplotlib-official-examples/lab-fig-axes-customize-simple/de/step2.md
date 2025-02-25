# Erstellen einer Figur und Festlegen des Hintergrunds

Wir werden eine Figur mit der `plt.figure()`-Methode erstellen, die eine `matplotlib.figure.Figure`-Instanz erstellt. Wir werden die Hintergrundfarbe der Figur mit der `rect.set_facecolor()`-Methode festlegen.

```python
fig = plt.figure()
rect = fig.patch  # eine Rechteckinstanz
rect.set_facecolor('lightgoldenrodyellow')
```

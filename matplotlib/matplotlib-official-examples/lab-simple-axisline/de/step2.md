# Figur und Teilgrafik erstellen

Als nächstes erstellen wir eine Figur und fügen eine Teilgrafik mit AxesZero hinzu. Dies erstellt eine Achse mit x- und y-Achsenbeschriftungen, aber ohne Striche oder Gitter.

```python
fig = plt.figure()
fig.subplots_adjust(right=0.85)
ax = fig.add_subplot(axes_class=AxesZero)
```

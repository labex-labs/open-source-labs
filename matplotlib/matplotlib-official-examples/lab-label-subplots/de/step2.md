# Teilbilder erstellen

Als nächstes erstellen wir die Teilbilder mit `plt.subplot_mosaic`. Wir werden ein 3x2-Gitter von Teilbildern erstellen und diese wie folgt beschriften:

- Das obere linke Diagramm wird als "a)" bezeichnet.
- Das untere linke Diagramm wird als "b)" bezeichnet.
- Die oberen rechten und unteren rechten Diagramme werden als "c)" und "d)" bezeichnet.

```python
fig, axs = plt.subplot_mosaic([['a)', 'c)'], ['b)', 'c)'], ['d)', 'd)']], layout='constrained')
```

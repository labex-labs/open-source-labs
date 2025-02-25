# Erzeuge das Diagramm

Jetzt, nachdem du die Daten generiert hast, wirst du das Diagramm mit der Funktion `imshow()` erstellen.

```python
fig, ax = plt.subplots()
im = ax.imshow(data2d)
ax.set_title('Pan on the colorbar to shift the color mapping\n'
             'Zoom on the colorbar to scale the color mapping')
```

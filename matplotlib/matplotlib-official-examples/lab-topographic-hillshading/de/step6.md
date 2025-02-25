# Bezeichnen des Diagramms

Wir bezeichnen die Zeilen und Spalten des Diagrammnetzes mit den Funktionen `set_title` und `set_ylabel`. Wir fügen auch einen Titel für die Gruppen der vertikalen Vergrößerung und des Mischmodus hinzu.

```python
for ax, ve in zip(axs[0], [0.1, 1, 10]):
    ax.set_title(f'{ve}', size=18)
for ax, mode in zip(axs[:, 0], ['Hillshade', 'hsv', 'overlay','soft']):
    ax.set_ylabel(mode, size=18)

axs[0, 1].annotate('Vertical Exaggeration', (0.5, 1), xytext=(0, 30),
                   textcoords='offset points', xycoords='axes fraction',
                   ha='center', va='bottom', size=20)
axs[2, 0].annotate('Blend Mode', (0, 0.5), xytext=(-30, 0),
                   textcoords='offset points', xycoords='axes fraction',
                   ha='right', va='center', size=20, rotation=90)
fig.subplots_adjust(bottom=0.05, right=0.95)
```

# Anpassen von Teilplots

Wir passen die Teilplots an, indem wir die Hintergrundfarbe der unteren Teilplots auf Schwarz setzen, die x-Achsenmarkierungen festlegen und jedem Teilplot einen Titel hinzufügen.

```python
axs[1, icol].set_facecolor('k')
axs[1, icol].xaxis.set_ticks(np.arange(0, 10, 2))
axs[0, icol].set_title(f'line widths (pts): {lwx:g}, {lwy:g}',
                       fontsize='medium')
```

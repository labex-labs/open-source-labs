# Füge vertikale Linien zum Histogramm hinzu

Um den Effekt der Schwellwertbildung leichter zu erkennen, werden wir vertikale Linien zum Histogramm hinzufügen, um die aktuellen Schwellwerte anzuzeigen. Wir werden zwei Linien für die untere und die obere Schwellenwerte erstellen.

```python
lower_limit_line = axs[1].axvline(slider.val[0], color='k')
upper_limit_line = axs[1].axvline(slider.val[1], color='k')
```

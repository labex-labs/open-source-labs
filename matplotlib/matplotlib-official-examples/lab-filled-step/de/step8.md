# Erstelle das mit Bezeichnung und Schraffierungen gefüllte Histogramm

Wir werden ein mit Bezeichnung und Schraffierungen gefülltes Histogramm erstellen, indem wir die zuvor definierte Funktion `stack_hist` verwenden. Wir werden die zuvor definierten Variablen `dict_data`, `color_cycle` und `hist_func` nutzen. Wir werden auch `labels` auf `['set 0','set 3']` setzen, um nur den ersten und den letzten Datensatz zu plotten.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True, sharey=True)
dict_data = dict(zip((c['label'] for c in label_cycle), stack_data))
arts = stack_hist(ax1, dict_data, color_cycle + hatch_cycle, hist_func=hist_func)

arts = stack_hist(ax2, dict_data, color_cycle + hatch_cycle, hist_func=hist_func, labels=['set 0','set 3'])
ax1.xaxis.set_major_locator(mticker.MaxNLocator(5))
ax1.set_xlabel('counts')
ax1.set_ylabel('x')
ax2.set_ylabel('x')
```

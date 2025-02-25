# Erstelle das mit Schraffierungen gefüllte Histogramm

Wir werden ein mit Schraffierungen gefülltes Histogramm erstellen, indem wir die zuvor definierte Funktion `stack_hist` verwenden. Wir werden die zuvor definierten Variablen `stack_data`, `color_cycle` und `hist_func` nutzen. Wir werden auch `plot_kwargs` so einstellen, dass die Kantenfarbe und die Orientierung eingeschlossen sind.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4.5), tight_layout=True)
arts = stack_hist(ax1, stack_data, color_cycle + label_cycle + hatch_cycle, hist_func=hist_func)

arts = stack_hist(ax2, stack_data, color_cycle, hist_func=hist_func, plot_kwargs=dict(edgecolor='w', orientation='h'))
ax1.set_ylabel('counts')
ax1.set_xlabel('x')
ax2.set_xlabel('counts')
ax2.set_ylabel('x')
```

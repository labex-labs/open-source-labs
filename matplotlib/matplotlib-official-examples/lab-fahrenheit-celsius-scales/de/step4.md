# Erstellen des Diagramms

Jetzt erstellen wir ein Diagramm mit zwei y-Achsen mithilfe der `subplots()`-Funktion von `matplotlib.pyplot`. Wir verbinden auch das `ylim_changed`-Ereignis der ersten Achse mit der `convert_ax_c_to_celsius()`-Funktion.

```python
fig, ax_f = plt.subplots()
ax_c = ax_f.twinx()

ax_f.callbacks.connect("ylim_changed", convert_ax_c_to_celsius)
```

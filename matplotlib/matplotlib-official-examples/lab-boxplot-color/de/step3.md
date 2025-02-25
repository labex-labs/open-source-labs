# Erstellen eines rechteckigen Boxplots

Wir werden nun einen rechteckigen Boxplot mit der `boxplot()`-Funktion in Matplotlib erstellen. Wir werden den Parameter `patch_artist` auf `True` setzen, um die Box mit Farbe zu füllen.

```python
fig, ax1 = plt.subplots(figsize=(9, 4))
bplot1 = ax1.boxplot(all_data,
                     vert=True,  # vertikale Boxausrichtung
                     patch_artist=True,  # mit Farbe füllen
                     labels=labels)  # x-Achsenbeschriftungen
ax1.set_title('Rechteckiger Boxplot')
```

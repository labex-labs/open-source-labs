# Erstellen eines gekerbten Boxplots

Wir werden nun einen gekerbten Boxplot mit der `boxplot()`-Funktion erstellen. Wir werden den Parameter `notch` auf `True` setzen, um einen gekerbten Boxplot zu erstellen.

```python
fig, ax2 = plt.subplots(figsize=(9, 4))
bplot2 = ax2.boxplot(all_data,
                     notch=True,  # Kerbform
                     vert=True,  # vertikale Boxausrichtung
                     patch_artist=True,  # mit Farbe füllen
                     labels=labels)  # x-Achsenbeschriftungen
ax2.set_title('Gekerbter Boxplot')
```

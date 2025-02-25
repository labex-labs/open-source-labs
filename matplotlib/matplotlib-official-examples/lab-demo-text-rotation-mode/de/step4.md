# Erzeuge die Subplots

Jetzt werden wir die Subplots mit der `subplots`-Funktion erstellen. Wir werden ein Gitter von Subplots mit dem gleichen Seitenverhältnis erstellen und die Markierungen auf den x- und y-Achsen entfernen. Wir werden auch eine vertikale und horizontale Linie in der Mitte jedes Subplots hinzufügen, um die Ausrichtung zu visualisieren.

```python
axs = fig.subplots(len(va_list), len(ha_list), sharex=True, sharey=True,
                   subplot_kw=dict(aspect=1),
                   gridspec_kw=dict(hspace=0, wspace=0))

for i, va in enumerate(va_list):
    for j, ha in enumerate(ha_list):
        ax = axs[i, j]
        ax.set(xticks=[], yticks=[])
        ax.axvline(0.5, color="skyblue", zorder=0)
        ax.axhline(0.5, color="skyblue", zorder=0)
        ax.plot(0.5, 0.5, color="C0", marker="o", zorder=1)
```

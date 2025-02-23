# Ein Diagramm mit Teildiagrammen erstellen

Jetzt werden wir ein Diagramm mit vier Teildiagrammen erstellen, eines für jeden Datensatz. Wir werden auch die x- und y-Bereiche für alle Teildiagramme gleich setzen.

```python
fig, axs = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(6, 6),
                        gridspec_kw={'wspace': 0.08, 'hspace': 0.08})
axs[0, 0].set(xlim=(0, 20), ylim=(2, 14))
axs[0, 0].set(xticks=(0, 10, 20), yticks=(4, 8, 12))
```

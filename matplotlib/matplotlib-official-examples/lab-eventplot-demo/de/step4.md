# Den ersten Ereignisplot erstellen - horizontale Ausrichtung

Wir werden den ersten Ereignisplot in einer horizontalen Ausrichtung erstellen.

```python
fig, axs = plt.subplots(2, 2)

axs[0, 0].eventplot(data1, colors=colors1, lineoffsets=lineoffsets1,
                    linelengths=linelengths1)
```

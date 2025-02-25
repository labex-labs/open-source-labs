# Erstellen der Figur und der Achsen

Wir werden eine Figur mit zwei Teilplots (Achsen) mithilfe der `subplots`-Funktion erstellen. Wir setzen auch den Titel der Figur.

```python
fig, axs = plt.subplots(2, 1)
fig.suptitle('Mouse Hover Over Figure or Axes to Trigger Events')
```

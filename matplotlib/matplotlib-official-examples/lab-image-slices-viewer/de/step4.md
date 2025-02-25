# Erstellen des Diagramms und Verbinden des Scrollereignisses

Wir werden das Diagramm mit der `subplots`-Funktion von Matplotlib erstellen und das erstellte `IndexTracker`-Objekt an sie übergeben. Anschließend verbinden wir das Scrollereignis mit der Figurcanvas mit `mpl_connect`.

```python
fig, ax = plt.subplots()
tracker = IndexTracker(ax, X)

fig.canvas.mpl_connect('scroll_event', tracker.on_scroll)
plt.show()
```

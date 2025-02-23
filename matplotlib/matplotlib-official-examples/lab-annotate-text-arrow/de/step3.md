# Ein Textpfeil hinzufügen, um die Richtung anzuzeigen

Um die Richtung der Daten anzuzeigen, fügen wir einen Textpfeil hinzu, indem wir die Funktion `ax.text()` und den Parameter `bbox` mit `boxstyle` auf "rarrow" setzen.

```python
bbox_props = dict(boxstyle="rarrow", fc=(0.8, 0.9, 0.9), ec="b", lw=2)
t = ax.text(0, 0, "Direction", ha="center", va="center", rotation=45,
            size=15,
            bbox=bbox_props)

bb = t.get_bbox_patch()
bb.set_boxstyle("rarrow", pad=0.6)
```

# Die x-Achse bei y = 0 sichtbar machen

Wir werden jetzt die x-Achse bei y = 0 sichtbar machen. Dies wird durch das Setzen der xzero-Achse auf sichtbar erreicht.

```python
ax.axis["xzero"].set_visible(True)
ax.axis["xzero"].label.set_text("Achse Null")
```

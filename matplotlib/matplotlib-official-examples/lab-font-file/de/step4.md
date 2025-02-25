# Setzen der Schriftart für den Titel

Wir setzen die Schriftart für den Titel des Graphen mit der `set_title()`-Methode der `Axes`-Klasse. Wir übergeben den Schriftartpfad als `font`-Parameter und den Namen der Schriftartdatei als Titel des Graphen.

```python
ax.set_title(f'Dies ist eine besondere Schriftart: {fpath.name}', font=fpath)
```

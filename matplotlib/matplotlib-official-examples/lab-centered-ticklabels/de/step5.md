# Ausrichten der Nebenstrichbeschriftungen

Schließlich müssen wir die Nebenstrichbeschriftungen in der Mitte zwischen den Hauptstrichen ausrichten. Wir können dies mit der `get_xticklabels()`-Funktion tun und das `minor`-Parameter auf `True` setzen, um die Nebenstrichbeschriftungen zu erhalten. Anschließend können wir durch die Beschriftungen iterieren und die horizontale Ausrichtung auf `'center'` setzen.

```python
# Ausrichten der Nebenstrichbeschriftung
for label in ax.get_xticklabels(minor=True):
    label.set_horizontalalignment('center')
imid = len(r) // 2
ax.set_xlabel(str(r.date[imid].item().year))
```

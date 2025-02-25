# Skalenbeschriftungsausrichtung anpassen

Schließlich können wir die Methoden `set_ha` und `set_va` verwenden, um die horizontale und vertikale Ausrichtung der Skalenbeschriftungen anzupassen.

```python
ax.axis["left"].major_ticklabels.set_ha("center")
ax.axis["bottom"].major_ticklabels.set_va("top")
```

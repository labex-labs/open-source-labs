# Hinzufügen von mehrzeiligem Text zum zweiten Teilplot

Im zweiten Teilplot werden wir mehrzeiligen Text mit der `text`-Funktion hinzufügen. Wir können die Position, die Größe, die vertikale und horizontale Ausrichtung sowie die Bounding Box (bbox) des Texts angeben.

```python
ax1.text(0.29, 0.4, "Mat\nTTp\n123", size=18,
         va="baseline", ha="right", multialignment="left",
         bbox=dict(fc="none"))

ax1.text(0.34, 0.4, "Mag\nTTT\n123", size=18,
         va="baseline", ha="left", multialignment="left",
         bbox=dict(fc="none"))

ax1.text(0.95, 0.4, "Mag\nTTT$^{A^A}$\n123", size=18,
         va="baseline", ha="right", multialignment="left",
         bbox=dict(fc="none"))
```

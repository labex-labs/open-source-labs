# Anmerkungen positionieren

Wir können die Anmerkungen mit unterschiedlichen Koordinatensystemen positionieren. Der folgende Code wird die Textanmerkung mit Datenkoordinaten und die Pfeilanmerkung mit Figurkoordinaten positionieren.

```python
ax.annotate("Data Point 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05),
            xycoords="data", textcoords="data")
ax.annotate("", xy=(1, 3), xytext=(0.5, 0.5),
            arrowprops=dict(facecolor="black", shrink=0.05),
            xycoords="data", textcoords="figure fraction")
```

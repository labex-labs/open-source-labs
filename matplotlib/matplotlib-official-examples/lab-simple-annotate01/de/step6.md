# Anmerkungen anpassen

Wir können die Anmerkungen anpassen, indem wir die Schriftgröße, die Schriftfarbe und den Pfeilstil ändern. Der folgende Code ändert die Schriftgröße, die Schriftfarbe und den Pfeilstil der Textanmerkung.

```python
ax.annotate("Data Point 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05, arrowstyle="->"),
            fontsize=12, color="red")
```

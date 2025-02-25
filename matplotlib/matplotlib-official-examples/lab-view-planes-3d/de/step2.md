# Definieren einer Funktion zum Anmerkungen der Achsen

Wir definieren eine Funktion `annotate_axes`, die wir später verwenden werden, um jede der primären 3D-Ansichtsebenen mit ihren jeweiligen Winkeln zu bezeichnen.

```python
def annotate_axes(ax, text, fontsize=18):
    ax.text(x=0.5, y=0.5, z=0.5, s=text,
            va="center", ha="center", fontsize=fontsize, color="black")
```

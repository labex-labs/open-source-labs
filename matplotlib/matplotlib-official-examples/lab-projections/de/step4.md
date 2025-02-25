# Die Daten darstellen

Stellen Sie die Daten auf jeder der drei Teilfiguren mit `plot_wireframe` dar.

```python
for ax in axs:
    ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```

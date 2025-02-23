# Erstellen eines doppelt logarithmischen Diagramms mit verstellbarem Datenbereich

Als nächstes erstellen wir ein doppelt logarithmisches Diagramm mit einem verstellbaren Datenbereich. Dies bedeutet, dass sowohl die x-Achse als auch die y-Achse logarithmische Skalen haben und das Seitenverhältnis des Diagramms so angepasst wird, dass die Daten gut dargestellt werden.

```python
fig, ax = plt.subplots()
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_adjustable("datalim")
ax.plot([1, 3, 10], [1, 9, 100], "o-")
ax.set_xlim(1e-1, 1e2)
ax.set_ylim(1e-1, 1e3)
ax.set_aspect(1)
ax.set_title("Log-Log Plot with Adjustable Datalim")
plt.show()
```

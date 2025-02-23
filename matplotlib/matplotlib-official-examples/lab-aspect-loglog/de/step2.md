# Erstellen eines doppelt logarithmischen Diagramms mit verstellbarem Rahmen

Als nächstes erstellen wir ein doppelt logarithmisches Diagramm mit einem verstellbaren Rahmen. Dies bedeutet, dass sowohl die x-Achse als auch die y-Achse logarithmische Skalen haben und das Seitenverhältnis des Diagramms 1 ist.

```python
fig, ax = plt.subplots()
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(1e1, 1e3)
ax.set_ylim(1e2, 1e3)
ax.set_aspect(1)
ax.set_title("Log-Log Plot with Adjustable Box")
plt.show()
```

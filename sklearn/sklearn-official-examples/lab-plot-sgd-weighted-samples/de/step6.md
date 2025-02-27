# Hinzufügen einer Legende und Anzeigen des Graphen

Wir fügen einer Legende zum Graphen hinzu, um zwischen dem ungewichteten und dem gewichteten Modell zu unterscheiden. Anschließend zeigen wir den Graphen an.

```python
no_weights_handles, _ = no_weights.legend_elements()
weights_handles, _ = samples_weights.legend_elements()
ax.legend(
    [no_weights_handles[0], weights_handles[0]],
    ["ohne Gewichte", "mit Gewichten"],
    loc="untere linke Ecke",
)

ax.set(xticks=(), yticks=())
plt.show()
```

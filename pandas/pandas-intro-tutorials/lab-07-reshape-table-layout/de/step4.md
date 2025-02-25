# Erstellen einer Pivot-Tabelle

Erstellen Sie eine Pivot-Tabelle, um die mittleren Konzentrationen von 𝑁𝑂2 und 𝑃𝑀25 in jedem der Stationen zu bestimmen.

```python
air_quality.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean"
)
```

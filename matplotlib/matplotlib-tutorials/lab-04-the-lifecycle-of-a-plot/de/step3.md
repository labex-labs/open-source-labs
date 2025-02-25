# Erstellen des Diagramms

Wir werden die Balkendiagrammvisualisierung verwenden, um die Verkaufsdaten darzustellen. Folgen Sie diesen Schritten:

1. Erstellen Sie eine Figur und ein Achsenobjekt mit `plt.subplots()`.

```python
fig, ax = plt.subplots()
```

2. Plotten Sie die Daten mit der `barh()`-Methode des Achsenobjekts.

```python
ax.barh(group_names, group_data)
```

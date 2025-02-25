# Erstellen einer Figur und eines Teilplots

Als nächstes müssen wir eine Figur und einen Teilplot für unser Diagramm erstellen. Wir werden das `projection`-Parameter von `add_subplot` verwenden, um ein Polarkoordinaten-Diagramm zu erstellen.

```python
fig = plt.figure()
ax = fig.add_subplot(projection="polar", facecolor="lightgoldenrodyellow")
```

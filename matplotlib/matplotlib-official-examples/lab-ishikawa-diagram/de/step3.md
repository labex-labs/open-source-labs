# Erstellen des Fishbone-Diagramms

Jetzt werden wir das Fishbone-Diagramm erstellen. Wir beginnen mit dem Erstellen eines Figure- und Axis-Objekts.

```python
fig, ax = plt.subplots(figsize=(10, 6), layout='constrained')
```

Als nächstes legen wir die x- und y-Bereiche für die Achse fest und deaktivieren die Achse.

```python
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')
```

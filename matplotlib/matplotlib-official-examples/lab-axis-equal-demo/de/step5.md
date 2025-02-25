# Automatische Anpassung der Datenbegrenzungen für gleichmäßiges Achsenverhältnis

Wir können auch die Funktion `set_aspect('equal', 'box')` verwenden, um die Datenbegrenzungen automatisch für ein gleichmäßiges Achsenverhältnis anzupassen.

```python
axs[1, 1].plot(3 * np.cos(an), 3 * np.sin(an))
axs[1, 1].set_aspect('equal', 'box')
axs[1, 1].set_title('noch ein Kreis, automatisch angepasste Datenbegrenzungen', fontsize=10)
```

Das resultierende Diagramm wird einen Kreis zeigen, der immer noch proportional und visuell ansprechend ist.

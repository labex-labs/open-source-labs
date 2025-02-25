# Anpassen des Diagramms

Um das Diagramm anzupassen, können wir die folgenden Methoden verwenden:

- `set_rmax`, um den maximalen Wert für `r` festzulegen
- `set_rticks`, um die Strichwerte für `r` festzulegen
- `set_rlabel_position`, um die Position der radialen Beschriftungen festzulegen

```python
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.set_rlabel_position(-22.5)
```

Wir können auch einen Titel für das Diagramm hinzufügen, indem wir die `set_title`-Methode verwenden.

```python
ax.set_title("A line plot on a polar axis", va='bottom')
```

Schließlich können wir einem Diagramm ein Gitter hinzufügen, indem wir die `grid`-Methode verwenden.

```python
ax.grid(True)
```

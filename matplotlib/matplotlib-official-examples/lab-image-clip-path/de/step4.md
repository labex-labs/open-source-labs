# Erstelle den Patch

Um den Patch zu erstellen, werden wir das `patches`-Modul von Matplotlib verwenden. Wir werden einen kreisförmigen Patch mit einem Radius von 200 Pixeln erstellen, der im Punkt (260, 200) zentriert ist.

```python
patch = patches.Circle((260, 200), radius=200, transform=ax.transData)
```

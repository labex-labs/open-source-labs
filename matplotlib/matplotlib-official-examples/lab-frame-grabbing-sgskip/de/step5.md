# Bilder aufnehmen und in eine Datei schreiben

Wir durchlaufen 100 Iterationen und generieren Zufallszahlen für die x- und y-Koordinaten. Wir aktualisieren die Daten für den Linienplot und nehmen das Bild mit dem Schreiber auf. Schließlich speichern wir die Bilder in eine Datei.

```python
x0, y0 = 0, 0

with writer.saving(fig, "writer_test.mp4", 100):
    for i in range(100):
        x0 += 0.1 * np.random.randn()
        y0 += 0.1 * np.random.randn()
        l.set_data(x0, y0)
        writer.grab_frame()
```

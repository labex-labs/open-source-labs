# Ein einfaches Diagramm generieren

Beginnen wir mit dem Erstellen eines einfachen Diagramms, indem wir die `plot`-Funktion in `pyplot` verwenden. In diesem Beispiel erstellen wir einen Liniendiagramm mit den y-Werten `[1, 2, 3, 4]`:

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
```

Erklärung:

- Wir importieren das `pyplot`-Modul aus `matplotlib` und geben es den Alias `plt`.
- Die `plot`-Funktion wird verwendet, um ein Liniendiagramm zu generieren. Indem wir eine einzelne Liste von y-Werten angeben, werden die x-Werte automatisch als `[0, 1, 2, 3]` generiert, da Python-Indizes bei 0 beginnen.
- Die `ylabel`-Funktion setzt die Bezeichnung für die y-Achse.
- Schließlich zeigt die `show`-Funktion das Diagramm an.

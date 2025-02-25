# Hinzufügen von Daten zum Plot

Wir fügen Daten zum Plot hinzu, indem wir die `plot`-Methode verwenden. Wir fügen drei Linien zum Plot hinzu, wobei jede Linie eine unterschiedliche y-Achse hat.

```python
p1, = ax.plot([0, 1, 2], [0, 1, 2], "C0", label="Density")
p2, = twin1.plot([0, 1, 2], [0, 3, 2], "C1", label="Temperature")
p3, = twin2.plot([0, 1, 2], [50, 30, 15], "C2", label="Velocity")
```

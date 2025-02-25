# Den Pfad erstellen

Als nächstes werden wir das `Path`-Objekt für die Bézier-Kurve erstellen. Das `Path`-Objekt nimmt eine Liste von Eckpunkten und Codes entgegen, die den Typ des Pfads zwischen den Eckpunkten angeben. In diesem Fall werden wir einen `MOVETO`-Code verwenden, um zum Startpunkt zu gelangen, gefolgt von zwei `CURVE3`-Codes, um die Kontrollpunkte und den Endpunkt anzugeben, und schließlich einen `CLOSEPOLY`-Code, um den Pfad zu schließen.

```python
Path = mpath.Path

bezier_path = Path([(0, 0), (1, 0), (1, 1), (0, 0)],
                   [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY])
```

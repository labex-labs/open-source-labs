# Hinzufügen von Daten

Wir werden die Daten zum Diagramm hinzufügen, indem wir die `plot`-Funktion verwenden. Wir werden jede Linie einer Variablen zuweisen, damit wir sie später referenzieren können.

```python
p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
p2, = par.plot([0, 1, 2], [0, 3, 2], label="Temperature")
```

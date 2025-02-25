# Die Daten plotten

Wir werden drei Datensätze auf dem gleichen Plot darstellen: Dichte, Temperatur und Geschwindigkeit. Wir werden die `plot()`-Funktion verwenden, um die Daten zu plotten.

```python
p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
p2, = par1.plot([0, 1, 2], [0, 3, 2], label="Temperature")
p3, = par2.plot([0, 1, 2], [50, 30, 15], label="Velocity")
```

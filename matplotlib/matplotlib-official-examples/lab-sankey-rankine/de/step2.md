# Definieren der Daten

Als nächstes definieren wir die Daten, die wir mit dem Sankey-Diagramm visualisieren möchten. In diesem Beispiel verwenden wir die Daten aus Beispiel 8.6 aus Morans und Shapiro's "Fundamentals of Engineering Thermodynamics". Die Daten repräsentieren den Energiefluss durch einen Rankine-Kraftzyklus. Wir definieren die Energieflüsse als Liste von Werten.

```python
Hdot = [260.431, 35.078, 180.794, 221.115, 22.700,
        142.361, 10.193, 10.210, 43.670, 44.312,
        68.631, 10.758, 10.758, 0.017, 0.642,
        232.121, 44.559, 100.613, 132.168]  # MW
```

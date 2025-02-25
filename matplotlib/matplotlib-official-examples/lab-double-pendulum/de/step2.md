# Parameter festlegen

Als nächstes definieren wir die Parameter für unsere Simulation. Diese Parameter umfassen die Gravitationsbeschleunigung, die Länge und Masse jedes Pendels sowie den Zeitintervall für die Simulation.

```python
G = 9.8  # Gravitationsbeschleunigung in m/s^2
L1 = 1.0  # Länge des ersten Pendels in m
L2 = 1.0  # Länge des zweiten Pendels in m
L = L1 + L2  # maximale Länge des kombinierten Pendels
M1 = 1.0  # Masse des ersten Pendels in kg
M2 = 1.0  # Masse des zweiten Pendels in kg
t_stop = 2.5  # Anzahl der zu simulierenden Sekunden
history_len = 500  # Anzahl der anzuzeigenden Trajektoriepunkte
```

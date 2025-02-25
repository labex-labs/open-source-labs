# Berechne die Position jedes Pendels

Wir verwenden nun die Position und Geschwindigkeit jedes Pendels in jedem Zeitschritt, um die x- und y-Koordinaten jedes Pendels zu berechnen.

```python
x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])

x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1
```

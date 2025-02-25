# Calcular la posición de cada péndulo

Ahora usaremos la posición y la velocidad de cada péndulo en cada paso de tiempo para calcular las coordenadas x e y de cada péndulo.

```python
x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])

x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1
```

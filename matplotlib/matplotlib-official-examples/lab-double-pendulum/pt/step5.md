# Calcular a Posição de Cada Pêndulo

Agora, usaremos a posição e a velocidade de cada pêndulo em cada passo de tempo para calcular as coordenadas x e y de cada pêndulo.

```python
x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])

x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1
```

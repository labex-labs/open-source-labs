# Вычисляем положение каждого маятника

Теперь мы будем использовать положение и скорость каждого маятника на каждом временном шаге для вычисления координат x и y каждого маятника.

```python
x1 = L1*sin(y[:, 0])
y1 = -L1*cos(y[:, 0])

x2 = L2*sin(y[:, 2]) + x1
y2 = -L2*cos(y[:, 2]) + y1
```

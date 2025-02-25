# Задаем начальные условия и интегрируем дифференциальное уравнение

Теперь мы зададим начальные условия для нашей моделирования. Мы зададим начальные углы и угловые скорости каждого маятника, а также интервал времени для моделирования. Затем мы интегрируем дифференциальное уравнение методом Эйлера, чтобы получить положение и скорость каждого маятника на каждом временном шаге.

```python
# create a time array from 0..t_stop sampled at 0.02 second steps
dt = 0.01
t = np.arange(0, t_stop, dt)

# th1 and th2 are the initial angles (degrees)
# w10 and w20 are the initial angular velocities (degrees per second)
th1 = 120.0
w1 = 0.0
th2 = -10.0
w2 = 0.0

# initial state
state = np.radians([th1, w1, th2, w2])

# integrate the ODE using Euler's method
y = np.empty((len(t), 4))
y[0] = state
for i in range(1, len(t)):
    y[i] = y[i - 1] + derivs(t[i - 1], y[i - 1]) * dt
```

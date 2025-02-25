# Configuration des paramètres

Ensuite, nous allons définir les paramètres de notre simulation. Ces paramètres incluent l'accélération due à la gravité, la longueur et la masse de chaque pendule, ainsi que l'intervalle de temps pour la simulation.

```python
G = 9.8  # acceleration due to gravity, in m/s^2
L1 = 1.0  # length of pendulum 1 in m
L2 = 1.0  # length of pendulum 2 in m
L = L1 + L2  # maximal length of the combined pendulum
M1 = 1.0  # mass of pendulum 1 in kg
M2 = 1.0  # mass of pendulum 2 in kg
t_stop = 2.5  # how many seconds to simulate
history_len = 500  # how many trajectory points to display
```

# Configuration des conditions initiales et intégration de l'EDO

Nous allons maintenant définir les conditions initiales de notre simulation. Nous allons fixer les angles initiaux et les vitesses angulaires de chaque pendule, ainsi que l'intervalle de temps de la simulation. Nous allons ensuite intégrer l'EDO en utilisant la méthode d'Euler pour obtenir la position et la vitesse de chaque pendule à chaque pas de temps.

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

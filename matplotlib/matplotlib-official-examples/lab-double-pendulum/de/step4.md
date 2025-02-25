# Anfangsbedingungen festlegen und die gewöhnliche Differentialgleichung (ODE) integrieren

Wir legen nun die Anfangsbedingungen für unsere Simulation fest. Wir setzen die Anfangswinkel und -winkelgeschwindigkeiten jedes Pendels sowie das Zeitintervall für die Simulation. Anschließend integrieren wir die ODE mit der Euler-Methode, um die Position und Geschwindigkeit jedes Pendels in jedem Zeitschritt zu erhalten.

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

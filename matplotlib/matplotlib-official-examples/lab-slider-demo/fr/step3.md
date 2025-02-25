# Créer le graphique initial

Maintenant, nous allons créer le graphique initial de l'onde sinusoïdale. Nous allons définir les paramètres initiaux pour l'amplitude et la fréquence et tracer l'onde sinusoïdale en utilisant ces paramètres.

```python
t = np.linspace(0, 1, 1000)
init_amplitude = 5
init_frequency = 3

fig, ax = plt.subplots()
line, = ax.plot(t, f(t, init_amplitude, init_frequency), lw=2)
ax.set_xlabel('Time [s]')
```

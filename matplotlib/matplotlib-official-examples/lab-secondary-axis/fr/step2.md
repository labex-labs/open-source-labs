# Tracez les données

Nous allons créer une simple onde sinusoïdale pour démontrer l'utilisation d'un axe secondaire. Nous allons tracer l'onde sinusoïdale en utilisant les degrés comme axe des abscisses.

```python
fig, ax = plt.subplots(layout='constrained')
x = np.arange(0, 360, 1)
y = np.sin(2 * x * np.pi / 180)
ax.plot(x, y)
ax.set_xlabel('angle [degrees]')
ax.set_ylabel('signal')
ax.set_title('Sine wave')
```

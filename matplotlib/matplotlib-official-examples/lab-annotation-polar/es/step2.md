# Crear un gráfico polar

A continuación, creamos un gráfico polar definiendo la figura y especificando que tiene una proyección polar. También definimos los valores de radio y theta que se utilizarán en la representación.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
r = np.arange(0, 1, 0.001)
theta = 2 * 2*np.pi * r
line, = ax.plot(theta, r, color='#ee8d18', lw=3)
```

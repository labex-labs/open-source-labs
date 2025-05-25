# Criar um Gráfico Polar

Em seguida, criamos um gráfico polar definindo a figura e especificando que ela tem uma projeção polar. Também definimos os valores de raio e theta a serem usados na plotagem.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
r = np.arange(0, 1, 0.001)
theta = 2 * 2*np.pi * r
line, = ax.plot(theta, r, color='#ee8d18', lw=3)
```

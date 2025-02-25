# Creando gráficos

Ahora, crearemos tres subgráficos usando la función `plt.subplots`. Dos gráficos se crearán en una figura, mientras que el tercer gráfico se creará en una figura separada.

```python
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(t, s1)
ax2.plot(t, s2)
fig, ax3 = plt.subplots()
ax3.plot(t, s3)
```

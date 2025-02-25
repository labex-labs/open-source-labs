# Crear el gráfico

Ahora, crearemos el gráfico utilizando `matplotlib`. Trazaremos las tres ondas senoidales en el mismo gráfico y estableceremos la visibilidad de la primera onda en `False` ya que queremos comenzar con ella oculta.

```python
fig, ax = plt.subplots()
l0, = ax.plot(t, s0, visible=False, lw=2, color='black', label='1 Hz')
l1, = ax.plot(t, s1, lw=2, color='red', label='2 Hz')
l2, = ax.plot(t, s2, lw=2, color='green', label='3 Hz')
fig.subplots_adjust(left=0.2)
```

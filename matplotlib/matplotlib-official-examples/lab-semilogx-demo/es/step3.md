# Crear un gráfico y establecer la escala logarítmica en el eje x

Creamos un objeto de figura y ejes utilizando el método `subplots()`. Luego graficamos la función de decaimiento exponencial utilizando el método `semilogx()` y establecemos la escala del eje x en una escala logarítmica utilizando el método `set_xscale()`. También agregamos una cuadrícula al gráfico utilizando el método `grid()`.

```python
fig, ax = plt.subplots()

ax.semilogx(t, np.exp(-t / 5.0))
ax.set_xscale('log')
ax.grid()
```

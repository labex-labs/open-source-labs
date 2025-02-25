# Crear la trama inicial

A continuación, creamos la trama inicial que se actualizará en función de la entrada del usuario. En este ejemplo, creamos una trama de una función con `t` como variable independiente.

```python
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)

t = np.arange(-2.0, 2.0, 0.001)
l, = ax.plot(t, np.zeros_like(t), lw=2)
```

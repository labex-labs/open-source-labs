# Crear ejes insertados

En este paso, creamos dos ejes insertados dentro de los ejes principales del gráfico utilizando `fig.add_axes`. Uno mostrará un histograma de los datos y el otro mostrará la respuesta impulso.

```python
# Create right inset axes
right_inset_ax = fig.add_axes([.65,.6,.2,.2], facecolor='k')
right_inset_ax.hist(s, 400, density=True)
right_inset_ax.set(title='Probabilidad', xticks=[], yticks=[])

# Create left inset axes
left_inset_ax = fig.add_axes([.2,.6,.2,.2], facecolor='k')
left_inset_ax.plot(t[:len(r)], r)
left_inset_ax.set(title='Respuesta impulso', xlim=(0,.2), xticks=[], yticks=[])
```

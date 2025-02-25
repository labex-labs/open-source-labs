# Crear entradas de leyenda con más de una clave de leyenda

En este paso, crearemos entradas de leyenda con más de una clave de leyenda.

```python
# Definir los datos para el gráfico
fig, (ax1, ax2) = plt.subplots(2, 1, layout='constrained')
p1 = ax1.scatter([1], [5], c='r', marker='s', s=100)
p2 = ax1.scatter([3], [2], c='b', marker='o', s=100)
p3, = ax1.plot([1, 5], [4, 4],'m-d')

# Crear una leyenda con dos claves para una entrada
l = ax1.legend([(p1, p3), p2], ['dos claves', 'una clave'], scatterpoints=1,
               numpoints=1, handler_map={tuple: HandlerTuple(ndivide=None)})

# Crear dos gráficos de barras uno encima del otro y cambiar el relleno entre las claves de la leyenda
x_left = [1, 2, 3]
y_pos = [1, 3, 2]
y_neg = [2, 1, 4]
rneg = ax2.bar(x_left, y_neg, width=0.5, color='w', hatch='///', label='-1')
rpos = ax2.bar(x_left, y_pos, width=0.5, color='k', label='+1')

# Tratar cada entrada de leyenda de manera diferente usando `HandlerTuple`s específicos
l = ax2.legend([(rpos, rneg), (rneg, rpos)], ['pad!=0', 'pad=0'],
               handler_map={(rpos, rneg): HandlerTuple(ndivide=None),
                            (rneg, rpos): HandlerTuple(ndivide=None, pad=0.)})

# Mostrar el gráfico
plt.show()
```

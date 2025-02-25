# Formateo simple

En este paso, mostraremos cómo usar un formateador simple pasando una cadena o una función a `~.Axis.set_major_formatter` o `~.Axis.set_minor_formatter`. Crearemos dos gráficas, una usando un formateador de cadena y la otra usando un formateador de función.

```python
fig0, axs0 = plt.subplots(2, 1, figsize=(8, 2))
fig0.suptitle('Formateo simple')

# Una ``str``, usando la sintaxis de la función de cadena de formato, se puede usar directamente como un
# formateador. La variable ``x`` es el valor de la marca y la variable ``pos`` es
# la posición de la marca. Esto crea un StrMethodFormatter automáticamente.
setup(axs0[0], título="'{x} km'")
axs0[0].xaxis.set_major_formatter('{x} km')

# Una función también se puede usar directamente como un formateador. La función debe tomar
# dos argumentos: ``x`` para el valor de la marca y ``pos`` para la posición de la marca,
# y debe devolver una ``str``. Esto crea un FuncFormatter automáticamente.
setup(axs0[1], título="lambda x, pos: str(x-5)")
axs0[1].xaxis.set_major_formatter(lambda x, pos: str(x-5))

fig0.tight_layout()
```

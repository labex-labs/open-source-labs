# Crear la gráfica

Utilizaremos la visualización de gráfico de barras para representar los datos de ventas. Siga estos pasos:

1. Cree una figura y un objeto de eje utilizando `plt.subplots()`.

```python
fig, ax = plt.subplots()
```

2. Trace los datos utilizando el método `barh()` del objeto de eje.

```python
ax.barh(group_names, group_data)
```

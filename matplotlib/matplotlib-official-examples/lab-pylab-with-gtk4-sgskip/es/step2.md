# Crear la figura y los gráficos

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], 'ro-', label='easy as 1 2 3')
ax.plot([1, 4, 9], 'gs--', label='easy as 1 2 3 squared')
ax.legend()
```

Creamos una figura con dos subgráficos y graficamos dos conjuntos de datos en ellos. También agregamos una leyenda a los gráficos.

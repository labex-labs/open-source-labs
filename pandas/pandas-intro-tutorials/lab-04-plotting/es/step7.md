# Crear subgráficos para cada columna

Podemos crear subgráficos separados para cada una de las columnas de datos utilizando el argumento `subplots`.

```python
# Creando subgráficos para cada columna
axs = air_quality.plot.area(figsize=(12, 4), subplots=True)
plt.show()
```

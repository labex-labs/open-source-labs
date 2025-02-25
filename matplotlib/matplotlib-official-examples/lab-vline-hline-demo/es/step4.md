# Crear el gráfico

Ahora, crearemos el gráfico usando la función `subplots` de Matplotlib. Crearemos dos subgráficos, uno para las líneas verticales y otro para las líneas horizontales. Estableceremos el tamaño de la figura en (12, 6) para una mejor visibilidad.

```python
# Create the plot
fig, (vax, hax) = plt.subplots(1, 2, figsize=(12, 6))
```

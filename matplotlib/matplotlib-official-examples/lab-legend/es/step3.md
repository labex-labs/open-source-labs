# Creando la trama

Ahora estamos listos para crear nuestra trama. Usaremos la función `plot` de Matplotlib para trazar tres líneas en la misma gráfica, cada una con una etiqueta predefinida. Usaremos el parámetro `label` para asignar las etiquetas a cada línea.

```python
# Create plots with pre-defined labels.
fig, ax = plt.subplots()
ax.plot(a, c, 'k--', label='Model length')
ax.plot(a, d, 'k:', label='Data length')
ax.plot(a, c + d, 'k', label='Total message length')
```

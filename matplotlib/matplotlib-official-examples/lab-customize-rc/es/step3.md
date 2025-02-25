# Crea subgráficos

Para crear subgráficos en Matplotlib, puedes utilizar el método `subplot()`. Este método toma tres argumentos: el número de filas, el número de columnas y el número del gráfico. Aquí te presento un ejemplo que crea tres subgráficos:

```python
plt.subplot(311)
plt.plot([1, 2, 3])

plt.subplot(312)
plt.plot([1, 2, 3])
plt.grid(True)

plt.subplot(313)
plt.plot([1, 2, 3])
plt.grid(True)
```

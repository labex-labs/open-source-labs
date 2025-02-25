# Apilando subgráficos en una dirección

Para crear múltiples subgráficos apilados vertical u horizontalmente, podemos pasar el número de filas y columnas como argumentos a la función `subplots()`. El objeto `axs` devuelto es una matriz de numpy de 1D que contiene la lista de `Axes` creados.

```python
fig, axs = plt.subplots(2)
axs[0].plot(x, y)
axs[1].plot(x, -y)
```

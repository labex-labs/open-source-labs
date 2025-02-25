# Apilando subgráficos en dos direcciones

Para crear una cuadrícula de subgráficos, podemos pasar el número de filas y columnas como argumentos a la función `subplots()`. El objeto `axs` devuelto es una matriz de NumPy de 2D.

```python
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].plot(x, y, 'tab:orange')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 1].plot(x, -y, 'tab:red')
```

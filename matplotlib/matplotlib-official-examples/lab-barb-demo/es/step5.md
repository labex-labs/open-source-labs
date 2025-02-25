# Crear un gráfico de barbas de viento con máscara

También podemos crear un gráfico de barbas de viento con máscara utilizando una matriz con máscara. En este caso, cambiaremos el valor de un vector a un valor incorrecto y lo mascaremos.

```python
masked_u = np.ma.masked_array(U)
masked_u[4] = 1000  # Valor incorrecto que no debe graficarse cuando se aplica la máscara
masked_u[4] = np.ma.masked

plt.barbs(X, Y, masked_u, V, length=8, pivot='middle')
plt.show()
```

# Crear subgráficos

Podemos crear subgráficos utilizando el método `plt.subplot()`. En este ejemplo, crearemos tres subgráficos, donde el primer subgráfico ocupará la primera fila y las tres columnas, y el segundo y tercer subgráfico ocuparán la segunda y tercera fila, respectivamente, y compartirán el eje x con el primer subgráfico.

```python
ax1 = plt.subplot(311)
ax2 = plt.subplot(312, sharex=ax1)
ax3 = plt.subplot(313, sharex=ax1, sharey=ax1)
```

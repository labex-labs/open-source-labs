# Comparar el comportamiento de "symlog" y "asinh" en el gráfico de muestra y = x

Compararemos el comportamiento de "symlog" y "asinh" en un gráfico de muestra y = x. Trazaremos el mismo gráfico dos veces, una vez con "symlog" y una vez con "asinh".

```python
fig1 = plt.figure()
ax0, ax1 = fig1.subplots(1, 2, sharex=True)

ax0.plot(x, x)
ax0.set_yscale('symlog')
ax0.grid()
ax0.set_title('symlog')

ax1.plot(x, x)
ax1.set_yscale('asinh')
ax1.grid()
ax1.set_title('asinh')
```

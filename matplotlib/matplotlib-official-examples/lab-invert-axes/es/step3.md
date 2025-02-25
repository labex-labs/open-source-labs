# Crear la gráfica

Ahora, podemos crear la gráfica utilizando Matplotlib. Usaremos la función `plot` para graficar nuestros datos y establecer los límites del eje x utilizando la función `set_xlim`.

```python
fig, ax = plt.subplots()

ax.plot(t, s)
ax.set_xlim(5, 0)  # decreasing time
ax.set_xlabel('decreasing time (s)')
ax.set_ylabel('voltage (mV)')
ax.set_title('Should be growing...')
ax.grid(True)

plt.show()
```

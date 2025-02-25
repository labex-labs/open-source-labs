# Trazar utilizando `.plot()`

Podemos lograr el mismo comportamiento que `.step()` utilizando el parámetro `drawstyle` de la función `.plot()`. Crearemos tres trazados utilizando diferentes valores para `drawstyle`.

```python
plt.plot(x, y + 2, drawstyle='steps', label='steps (=steps-pre)')
plt.plot(x, y + 1, drawstyle='steps-mid', label='steps-mid')
plt.plot(x, y, drawstyle='steps-post', label='steps-post')
plt.legend()
plt.show()
```

El código anterior creará un trazado con tres curvas de valores constantes por segmentos, cada una con un valor diferente para `drawstyle`.

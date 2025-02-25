# Trazar utilizando `.step()`

Podemos utilizar la función `.step()` para crear curvas de valores constantes por segmentos. El parámetro `where` determina dónde deben dibujarse los pasos. Crearemos tres trazados utilizando diferentes valores para `where`.

```python
plt.step(x, y + 2, label='pre (default)', where='pre')
plt.step(x, y + 1, label='mid', where='mid')
plt.step(x, y, label='post', where='post')
plt.legend()
plt.show()
```

El código anterior creará un trazado con tres curvas de valores constantes por segmentos, cada una con un valor diferente para `where`.

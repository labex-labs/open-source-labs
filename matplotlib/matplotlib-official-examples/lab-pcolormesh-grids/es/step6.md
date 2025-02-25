# Sombreado automático

Es posible que el usuario desee que el código elija automáticamente cuál usar. En este caso, `shading='auto'` decidirá si usar el sombreado `flat` o `nearest` en función de las formas de `X`, `Y` y `Z`. Podemos visualizar la grilla usando el siguiente bloque de código:

```python
fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z, shading='auto', cmap='viridis')
ax.set_title('Auto Shading')
plt.show()
```

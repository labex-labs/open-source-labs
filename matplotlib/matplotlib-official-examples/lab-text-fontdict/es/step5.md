# Agregar texto al gráfico

Podemos agregar texto a nuestro gráfico utilizando la función text(). En este ejemplo, agregaremos una expresión LaTeX al gráfico utilizando el diccionario de fuentes para personalizar el estilo.

```python
plt.text(2, 0.65, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
```

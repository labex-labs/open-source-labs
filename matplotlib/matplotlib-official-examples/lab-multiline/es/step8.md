# Personalizando las etiquetas del eje X

Para personalizar las etiquetas del eje x, podemos utilizar la función `set_xticks`. Podemos especificar las posiciones y las etiquetas de las marcas.

```python
ax1.set_xticks([0.2, 0.4, 0.6, 0.8, 1.],
               labels=["Jan\n2009", "Feb\n2009", "Mar\n2009", "Apr\n2009",
                       "May\n2009"])
```

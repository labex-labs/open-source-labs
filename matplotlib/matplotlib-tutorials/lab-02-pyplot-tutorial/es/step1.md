# Generando un gráfico simple

Para comenzar, generemos un gráfico simple utilizando la función `plot` en `pyplot`. En este ejemplo, graficaremos una gráfica de líneas con los valores de y `[1, 2, 3, 4]`:

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
```

Explicación:

- Importamos el módulo `pyplot` de `matplotlib` y lo aliasamos como `plt`.
- La función `plot` se utiliza para generar una gráfica de líneas. Al proporcionar una sola lista de valores de y, los valores de x se generan automáticamente como `[0, 1, 2, 3]`, ya que los rangos de Python comienzan en 0.
- La función `ylabel` establece la etiqueta para el eje y.
- Finalmente, la función `show` muestra el gráfico.

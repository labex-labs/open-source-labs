# Trabajo interactivo rápido

Para un trabajo interactivo rápido, los píxeles suelen ser una buena unidad de tamaño. Podemos utilizar el valor predeterminado de dpi de 100 para convertir valores de píxeles a pulgadas. Luego podemos utilizar este valor como el parámetro figsize en la función subplots. El código siguiente muestra cómo crear una figura con un tamaño de 6 pulgadas x 2 pulgadas utilizando valores de píxeles.

```python
plt.subplots(figsize=(600/100, 200/100))
plt.show()
```

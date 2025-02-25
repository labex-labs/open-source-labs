# Agregando la leyenda

Para agregar la leyenda a nuestra trama, usamos la función `legend` de Matplotlib. Pasamos el parámetro `loc` para especificar la ubicación de la leyenda y el parámetro `shadow` para agregar un efecto de sombra a la leyenda. También usamos el parámetro `fontsize` para establecer el tamaño de fuente de la leyenda.

```python
legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')
```

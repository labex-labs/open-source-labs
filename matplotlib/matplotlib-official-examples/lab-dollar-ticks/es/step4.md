# Personalizar los Parámetros de las Marcas de Escala

También podemos personalizar los parámetros de las marcas de escala (ticks) para ajustar aún más la apariencia de nuestro gráfico. En este ejemplo, cambiaremos el color de las etiquetas de las marcas de escala a verde y las moveremos al lado derecho del gráfico.

```python
# Customize tick parameters
ax.tick_params(axis='y', which='major', labelcolor='green', labelright=True)
```

En el código anterior, utilizamos el método `tick_params` para personalizar los parámetros de las marcas de escala del eje y. Establecemos el parámetro `axis` en `'y'` para especificar que estamos personalizando el eje y, y el parámetro `which` en `'major'` para especificar que estamos personalizando las marcas de escala principales. Establecemos el parámetro `labelcolor` en `'green'` para cambiar el color de las etiquetas de las marcas de escala, y el parámetro `labelright` en `True` para mover las etiquetas de las marcas de escala al lado derecho del gráfico.

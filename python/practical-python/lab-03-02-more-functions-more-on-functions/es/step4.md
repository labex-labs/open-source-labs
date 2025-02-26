# Mejores prácticas de diseño

Siempre dé nombres cortos, pero significativos a los argumentos de las funciones.

Alguien que use una función puede querer usar el estilo de llamada con palabras clave.

```python
d = read_prices('prices.csv', debug=True)
```

Las herramientas de desarrollo de Python mostrarán los nombres en las características de ayuda y la documentación.

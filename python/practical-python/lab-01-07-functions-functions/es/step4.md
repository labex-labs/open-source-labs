# Capturar y manejar excepciones

Las excepciones pueden ser capturadas y manejadas.

Para capturar, use la instrucción `try - except`.

```python
for line in file:
    fields = line.split(',')
    try:
        shares = int(fields[1])
    except ValueError:
        print("Couldn't parse", line)
  ...
```

El nombre `ValueError` debe coincidir con el tipo de error que se está intentando capturar.

A menudo es difícil saber exactamente qué tipos de errores pueden ocurrir con anticipación, dependiendo de la operación que se está realizando. Por mejor o por peor, el manejo de excepciones a menudo se agrega _después_ de que un programa se ha detenido inesperadamente (es decir, "oh, olvidamos capturar ese error. Deberíamos manejarlo!").

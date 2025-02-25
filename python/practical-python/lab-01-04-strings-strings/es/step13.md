# Ejercicio 1.14: Concatenación de cadenas

Aunque los datos de cadena son de solo lectura, siempre puedes reasignar una variable a una cadena recién creada.

Prueba la siguiente declaración que concatena un nuevo símbolo "GOOG" al final de `symbols`:

```python
>>> symbols = symbols + 'GOOG'
>>> symbols
'AAPL,IBM,MSFT,YHOO,SCOGOOG'
>>>
```

Uy! Eso no es lo que querías. Corrige it para que la variable `symbols` tenga el valor `'AAPL,IBM,MSFT,YHOO,SCO,GOOG'`.

```python
>>> symbols =?
>>> symbols
'AAPL,IBM,MSFT,YHOO,SCO,GOOG'
>>>
```

Agrega `'HPQ'` al principio de la cadena:

```python
>>> symbols =?
>>> symbols
'HPQ,AAPL,IBM,MSFT,YHOO,SCO,GOOG'
>>>
```

En estos ejemplos, puede parecer que la cadena original está siendo modificada, en una aparente violación de la propiedad de solo lectura de las cadenas. No es así. Las operaciones en cadenas crean una cadena completamente nueva cada vez. Cuando la variable `symbols` se reasigna, apunta a la cadena recién creada. Después, la cadena vieja se destruye ya que ya no se está utilizando.

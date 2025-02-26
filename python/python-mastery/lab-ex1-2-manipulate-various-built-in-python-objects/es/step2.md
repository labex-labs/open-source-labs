# Parte 2 : Manipulación de Cadenas

Defina una cadena que contenga una serie de símbolos de cotización de acciones como esta:

```python
>>> symbols = 'AAPL IBM MSFT YHOO SCO'
```

Ahora, experimentemos con diferentes operaciones de cadenas:

## Extracción de caracteres individuales y subcadenas

Las cadenas son arrays de caracteres. Intente extraer algunos caracteres:

```python
>>> symbols[0]
'A'
>>> symbols[1]
'A'
>>> symbols[2]
'P'
>>> symbols[-1]        # Último carácter
'O'
>>> symbols[-2]        # 2º carácter contando desde el final
'C'
>>>
```

Intente tomar algunas subcadenas:

```python
>>> symbols[:4]
'AAPL'
>>> symbols[-3:]
'SCO'
>>> symbols[5:8]
'IBM'
>>>
```

## Cadenas como objetos de solo lectura

Las cadenas son de solo lectura. Verifíquelo intentando cambiar el primer carácter de `symbols` a una 'a' en minúsculas.

```python
>>> symbols[0] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```

## Concatenación de cadenas

Aunque los datos de cadena son de solo lectura, siempre puede reasignar una variable a una cadena recién creada.
Intente la siguiente declaración que concatena un nuevo símbolo "GOOG" al final de `symbols`:

```python
>>> symbols += ' GOOG'
>>> symbols
... observe el resultado...
```

Ahora, intente agregar "HPQ" al principio de `symbols` de la siguiente manera:

```python
>>> symbols = 'HPQ'+ symbols
>>> symbols
... observe el resultado...
```

Debe tenerse en cuenta en ambos estos ejemplos que la cadena original `symbols` _NO_ se está modificando "in place". En lugar de eso, se crea una cadena completamente nueva. El nombre de variable `symbols` solo se asocia con el resultado. Después, la antigua cadena se destruye ya que ya no se está utilizando.

## Prueba de pertenencia (prueba de subcadena)

Experimente con el operador `in` para comprobar subcadenas. En el prompt interactivo, pruebe estas operaciones:

```python
>>> 'IBM' in symbols
True
>>> 'AA' in symbols
True
>>> 'CAT' in symbols
False
>>>
```

Asegúrese de entender por qué la búsqueda de "AA" devolvió `True`.

## Métodos de cadena

En el prompt interactivo de Python, intente experimentar con algunos de los métodos de cadena.

```python
>>> symbols.lower()
'hpq aapl ibm msft yhoo sco goog'
>>> symbols
'HPQ AAPL IBM MSFT YHOO SCO GOOG'
```

Recuerde, las cadenas siempre son de solo lectura. Si desea guardar el resultado de una operación, debe colocarlo en una variable:

```python
>>> lowersyms = symbols.lower()
>>> lowersyms
'hpq aapl ibm msft yhoo sco goog'
>>>
```

Pruebe algunas operaciones más:

```python
>>> symbols.find('MSFT')
13
>>> symbols[13:17]
'MSFT'
>>> symbols = symbols.replace('SCO','')
>>> symbols
'HPQ AAPL IBM MSFT YHOO  GOOG'
>>>
```

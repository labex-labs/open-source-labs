# Ejercicio 2.1: Tuplas

En el prompt interactivo, cree la siguiente tupla que representa la fila anterior, pero con las columnas numéricas convertidas a números adecuados:

```python
>>> t = (row[0], int(row[1]), float(row[2]))
>>> t
('AA', 100, 32.2)
>>>
```

Con esto, ahora puede calcular el costo total multiplicando las acciones y el precio:

```python
>>> cost = t[1] * t[2]
>>> cost
3220.0000000000005
>>>
```

¿Está rota la matemática en Python? ¿Qué pasa con la respuesta de 3220.0000000000005?

Este es un artefacto del hardware de punto flotante de su computadora que solo puede representar con precisión decimales en Base-2, no en Base-10. Para cálculos tan simples que involucran decimales en Base-10, se introducen pequeños errores. Esto es normal, aunque quizás un poco sorprendente si nunca lo ha visto antes.

Esto sucede en todos los lenguajes de programación que usan decimales de punto flotante, pero a menudo se oculta al imprimir. Por ejemplo:

```python
>>> print(f'{cost:0.2f}')
3220.00
>>>
```

Las tuplas son de solo lectura. Verifíquelo intentando cambiar el número de acciones a 75.

```python
>>> t[1] = 75
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
```

Aunque no puede cambiar el contenido de la tupla, siempre puede crear una tupla completamente nueva que reemplace a la vieja.

```python
>>> t = (t[0], 75, t[2])
>>> t
('AA', 75, 32.2)
>>>
```

Cada vez que reasigna un nombre de variable existente de esta manera, el valor antiguo se descarta. Aunque la asignación anterior puede parecer que está modificando la tupla, en realidad está creando una nueva tupla y desechando la vieja.

Las tuplas a menudo se usan para empacar y desempaquetar valores en variables. Pruebe lo siguiente:

```python
>>> name, shares, price = t
>>> name
'AA'
>>> shares
75
>>> price
32.2
>>>
```

Tome las variables anteriores y empáquelas nuevamente en una tupla

```python
>>> t = (name, 2*shares, price)
>>> t
('AA', 150, 32.2)
>>>
```

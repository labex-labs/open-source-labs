# Trabajando con múltiples objetos Stock

En la programación orientada a objetos, una clase es como un modelo (blueprint), y las instancias de esa clase son los objetos reales creados a partir de ese modelo. Nuestra clase `Stock` es un modelo para representar acciones (stocks). Podemos crear múltiples instancias de esta clase `Stock` para representar diferentes acciones. Cada instancia tendrá su propio conjunto de atributos, como el nombre de la acción, el número de acciones y el precio por acción.

1. Con la sesión interactiva de Python todavía en ejecución, vamos a crear otro objeto `Stock`. Esta vez, representará a IBM. Para crear una instancia de la clase `Stock`, llamamos al nombre de la clase como si fuera una función y pasamos los argumentos necesarios. Los argumentos aquí son el nombre de la acción, el número de acciones y el precio por acción.

```python
t = Stock('IBM', 50, 91.5)
```

En esta línea de código, estamos creando un nuevo objeto `Stock` llamado `t` que representa a IBM. Tiene 50 acciones, y cada acción cuesta $91.5.

2. Ahora, queremos calcular el costo de esta nueva acción. La clase `Stock` tiene un método llamado `cost()` que calcula el costo total de la acción multiplicando el número de acciones por el precio por acción.

```python
t.cost()
```

Cuando ejecutes este código, Python llamará al método `cost()` en el objeto `t` y devolverá el costo total.

Salida:

```
4575.0
```

3. Podemos formatear y mostrar la información de nuestras acciones de una manera agradable y organizada utilizando el formato de cadenas (string formatting) de Python. El formato de cadenas nos permite especificar cómo se deben presentar diferentes tipos de datos en una cadena.

```python
print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
```

En este código, estamos utilizando el formato de cadenas de estilo antiguo en Python. El operador `%` se utiliza para sustituir valores en una plantilla de cadena. La plantilla de cadena `'%10s %10d %10.2f'` define cómo se deben formatear el nombre de la acción, el número de acciones y el precio.

Salida:

```
      GOOG        100     490.10
```

Esta cadena formateada funciona de la siguiente manera:

- `%10s` formatea una cadena en un campo de 10 caracteres de ancho (alineado a la derecha). Esto significa que el nombre de la acción se colocará en un espacio de 10 caracteres de ancho y estará alineado a la derecha dentro de ese espacio.
- `%10d` formatea un entero en un campo de 10 caracteres de ancho. Entonces, el número de acciones se colocará en un espacio de 10 caracteres de ancho.
- `%10.2f` formatea un número de punto flotante con 2 decimales en un campo de 10 caracteres de ancho. El precio se mostrará con dos decimales y se colocará en un espacio de 10 caracteres de ancho.

4. Ahora, formateemos la información de las acciones de IBM de la misma manera. Solo necesitamos reemplazar el nombre del objeto de `s` a `t` en el código de formato de cadenas.

```python
print('%10s %10d %10.2f' % (t.name, t.shares, t.price))
```

Salida:

```
       IBM         50      91.50
```

5. En Python moderno, también podemos usar f - cadenas (f - strings) para el formato. Las f - cadenas son más legibles y fáciles de usar. Comparemos los costos de ambas acciones utilizando f - cadenas.

```python
print(f"Google stock costs ${s.cost()}, IBM stock costs ${t.cost()}")
```

En esta f - cadena, estamos incrustando directamente expresiones dentro de llaves `{}`. Python evaluará estas expresiones e insertará los resultados en la cadena.

Salida:

```
Google stock costs $49010.0, IBM stock costs $4575.0
```

6. Cuando hayas terminado de experimentar, es hora de salir del modo interactivo de Python. Puedes hacer esto utilizando la función `exit()`.

```python
exit()
```

Cada objeto `Stock` mantiene su propio conjunto de atributos, lo que demuestra cómo funcionan las instancias de clase en la programación orientada a objetos. Esto nos permite crear múltiples objetos de acciones, cada uno con valores diferentes, mientras comparten los mismos métodos.

# Modo interactivo

Cuando se inicia Python, se obtiene un _modo interactivo_ donde se puede experimentar.

Si se empieza a escribir declaraciones, se ejecutarán inmediatamente. No hay un ciclo de edición/compilación/ejecución/depuración.

```python
>>> print('hello world')
hello world
>>> 37*42
1554
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
>>>
```

Este llamado _read-eval-print-loop_ (o REPL) es muy útil para la depuración y la exploración.

**PARA DEJAR DE HACER**: Si no se puede entender cómo interactuar con Python, detenga lo que está haciendo y averigüe cómo hacerlo. Si se está usando un IDE, puede estar oculto detrás de una opción de menú u otra ventana. Muchas partes de este curso asumen que se puede interactuar con el intérprete.

Echemos un vistazo más detenido a los elementos del REPL:

- `>>>` es el indicador del intérprete para comenzar una nueva declaración.
- `...` es el indicador del intérprete para continuar una declaración. Presione Enter en una línea en blanco para terminar de escribir y ejecutar lo que ha introducido.

El indicador `...` puede o no aparecer según el entorno. Para este curso, se muestra como espacios en blanco para facilitar la copia/pega de los ejemplos de código.

El subrayado `_` guarda el último resultado.

```python
>>> 37 * 42
1554
>>> _ * 2
3108
>>> _ + 50
3158
>>>
```

_esto solo es cierto en el modo interactivo_. Nunca se utiliza `_` en un programa.

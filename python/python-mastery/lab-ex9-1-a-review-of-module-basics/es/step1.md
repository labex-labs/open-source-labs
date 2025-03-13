# Creación de un módulo simple

Comencemos nuestro viaje por los módulos de Python creando uno simple. En Python, un módulo es esencialmente un archivo con extensión `.py` que contiene código de Python. Piénsalo como un contenedor donde puedes agrupar funciones, clases y variables relacionadas. Esto hace que tu código esté más organizado y sea más fácil de gestionar, especialmente a medida que tus proyectos aumentan de tamaño.

1. Primero, abre el WebIDE. Una vez abierto, necesitarás crear un nuevo archivo. Para hacer esto, haz clic en "File" en la barra de menú y luego selecciona "New File". Nombrar este nuevo archivo `simplemod.py` y guárdalo en el directorio `/home/labex/project`. Este es el directorio donde guardaremos todos los archivos relacionados con este experimento.

2. Ahora, agreguemos algo de código a nuestro recién creado archivo `simplemod.py`. El código siguiente define algunos elementos básicos que comúnmente encontrarás en un módulo de Python.

```python
# simplemod.py

x = 42        # Una variable global

# Una función simple
def foo():
    print('x is', x)

# Una clase simple
class Spam:
    def yow(self):
        print('Yow!')

# Una declaración de script
print('Loaded simplemod')
```

En este código:

- `x = 42` crea una variable global llamada `x` y le asigna el valor `42`. Las variables globales se pueden acceder desde cualquier lugar dentro del módulo.
- La función `foo()` se define para imprimir el valor de la variable global `x`. Las funciones son bloques de código reutilizables que realizan una tarea específica.
- La clase `Spam` es un modelo para crear objetos. Tiene un método llamado `yow()`, que simplemente imprime la cadena 'Yow!'. Los métodos son funciones que pertenecen a una clase.
- La declaración `print('Loaded simplemod')` es una declaración de script. Se ejecutará tan pronto como se cargue el módulo, lo que nos ayuda a confirmar que el módulo se ha cargado correctamente.

3. Después de agregar el código, guarda el archivo. Puedes hacer esto presionando `Ctrl+S` en tu teclado o seleccionando "File" > "Save" del menú. Guardar el archivo asegura que todos los cambios que hayas realizado se conserven.

Echemos un vistazo más detallado a lo que contiene este módulo:

- Una variable global `x` con el valor `42`. Esta variable se puede usar en todo el módulo e incluso acceder desde otros módulos si se importa correctamente.
- Una función `foo()` que imprime el valor de `x`. Las funciones son útiles para realizar tareas repetitivas sin tener que escribir el mismo código varias veces.
- Una clase `Spam` con un método `yow()`. Las clases y los métodos son conceptos fundamentales en la programación orientada a objetos, que te permite crear estructuras de datos y comportamientos complejos.
- Una declaración `print` que se ejecuta cuando se carga el módulo. Esta declaración sirve como indicador visual de que el módulo se ha cargado correctamente en el entorno de Python.

La declaración `print` al final nos ayudará a observar cuándo se carga el módulo, lo cual es importante para la depuración y la comprensión de cómo funcionan los módulos en Python.

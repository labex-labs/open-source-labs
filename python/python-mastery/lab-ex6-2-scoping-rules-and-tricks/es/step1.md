# Comprender el problema con la inicialización de clases

En el mundo de la programación, las clases son un concepto fundamental que te permite crear tipos de datos personalizados. En ejercicios anteriores, es posible que hayas creado una clase `Structure`. Esta clase es una herramienta útil para definir fácilmente estructuras de datos. Una estructura de datos es una forma de organizar y almacenar datos para que se puedan acceder y utilizar de manera eficiente. La clase `Structure`, como clase base, se encarga de inicializar atributos basados en una lista predefinida de nombres de campos. Los atributos son variables que pertenecen a un objeto, y los nombres de campos son los nombres que le damos a estos atributos.

Echemos un vistazo más detallado a la implementación actual de la clase `Structure`. Para hacer esto, necesitamos abrir el archivo `structure.py` en el editor de código. Este archivo contiene el código de la clase `Structure`. Aquí están los comandos para navegar al directorio del proyecto y abrir el archivo:

```bash
cd ~/project
code structure.py
```

La clase `Structure` proporciona un marco básico para definir estructuras de datos simples. Cuando creamos una subclase, como la clase `Stock`, podemos definir los campos específicos que queremos para esa subclase. Una subclase hereda las propiedades y métodos de su clase base, en este caso, la clase `Structure`. Por ejemplo, en la clase `Stock`, definimos los campos `name`, `shares` y `price`:

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')
```

Ahora, abramos el archivo `stock.py` para ver cómo se implementa la clase `Stock` en el contexto del código general. Es probable que este archivo contenga el código que utiliza la clase `Stock` e interactúa con ella. Utiliza el siguiente comando para abrir el archivo:

```bash
code stock.py
```

Aunque este enfoque de usar la clase `Structure` y sus subclases funciona, tiene varias limitaciones. Para identificar estos problemas, ejecutaremos el intérprete de Python y exploraremos cómo se comporta la clase `Stock`. El siguiente comando importará la clase `Stock` y mostrará su información de ayuda:

```bash
python3 -c "from stock import Stock; help(Stock)"
```

Cuando ejecutes este comando, notarás que la firma mostrada en la salida de ayuda no es muy útil. En lugar de mostrar los nombres reales de los parámetros como `name`, `shares` y `price`, solo muestra `*args`. Esta falta de nombres de parámetros claros dificulta que los usuarios comprendan cómo crear correctamente una instancia de la clase `Stock`.

Intentemos también crear una instancia de `Stock` utilizando argumentos de palabra clave. Los argumentos de palabra clave te permiten especificar los valores de los parámetros por sus nombres, lo que puede hacer el código más legible. Ejecuta el siguiente comando:

```bash
python3 -c "from stock import Stock; s = Stock(name='GOOG', shares=100, price=490.1); print(s)"
```

Deberías obtener un mensaje de error como este:

```
TypeError: __init__() got an unexpected keyword argument 'name'
```

Este error se produce porque nuestro método `__init__` actual, que es responsable de inicializar objetos de la clase `Stock`, no maneja argumentos de palabra clave. Solo acepta argumentos posicionales, lo que significa que debes proporcionar los valores en un orden específico sin usar los nombres de los parámetros. Esta es una limitación que queremos solucionar en este laboratorio.

En este laboratorio, exploraremos diferentes enfoques para hacer que nuestra clase `Structure` sea más flexible y amigable para el usuario. Al hacerlo, podemos mejorar la usabilidad de la clase `Stock` y otras subclases de `Structure`.

# Comprender los módulos de Python

En Python, un módulo es como un contenedor que almacena definiciones y declaraciones de Python. Es esencialmente un archivo, y el nombre de este archivo es el nombre del módulo con la extensión `.py` agregada al final. Puedes pensar en los módulos como cajas de herramientas. Te ayudan a organizar tu código de Python de manera lógica, lo que facilita su reutilización y mantenimiento. Al igual que guardarías diferentes herramientas en cajas separadas para una mejor organización, puedes agrupar código de Python relacionado en diferentes módulos.

Echemos un vistazo a los archivos que se han configurado para este laboratorio:

1. Primero, abriremos el archivo `stock.py` en el editor para ver su contenido. Para hacer esto, usaremos los siguientes comandos. El comando `cd` cambia el directorio al directorio `project` donde se encuentra nuestro archivo, y el comando `cat` muestra el contenido del archivo.

```bash
cd ~/project
cat stock.py
```

Este archivo `stock.py` define una clase `Stock`. Una clase es como un plano para crear objetos. En este caso, la clase `Stock` representa una acción. Tiene atributos (que son como características) para el nombre de la acción, el número de acciones y el precio. También tiene un método (que es como una función asociada a la clase) para calcular el costo de la acción.

2. A continuación, examinemos el archivo `pcost.py`. Usaremos el comando `cat` nuevamente para ver su contenido.

```bash
cat pcost.py
```

Este archivo define una función llamada `portfolio_cost()`. Una función es un bloque de código que realiza una tarea específica. La función `portfolio_cost()` lee un archivo de cartera y calcula el costo total de todas las acciones en esa cartera.

3. Ahora, echemos un vistazo a los datos de muestra de la cartera. Usaremos el comando `cat` para ver el contenido del archivo `portfolio.dat`.

```bash
cat portfolio.dat
```

Este archivo contiene datos de acciones en un formato simple. Cada línea tiene el símbolo de cotización de la acción, el número de acciones y el precio por acción.

## Usar la declaración import

La declaración `import` de Python es una herramienta poderosa que te permite usar código de otros módulos en tu programa actual. Es como pedir prestadas herramientas de otras cajas de herramientas. Practiquemos el uso de diferentes formas de importar código:

1. Primero, necesitamos iniciar el intérprete de Python. El intérprete de Python es un programa que ejecuta código de Python. Usaremos el siguiente comando para iniciarlo.

```bash
python3
```

2. Ahora, importemos el módulo `pcost` y veamos qué sucede. Cuando usamos la declaración `import`, Python busca el archivo `pcost.py` y hace que el código dentro de él esté disponible para que lo usemos.

```python
import pcost
```

Deberías ver la salida `44671.15`. Este es el costo calculado de la cartera del archivo `portfolio.dat`. Cuando se importa el módulo `pcost`, el código al final del archivo `pcost.py` se ejecuta automáticamente.

3. Intentemos llamar a la función `portfolio_cost()` con un archivo de cartera diferente. Usaremos la sintaxis `pcost.portfolio_cost()` para llamar a la función del módulo `pcost`.

```python
pcost.portfolio_cost('portfolio2.dat')
```

La salida debe ser `19908.75`, que representa el costo total de las acciones en el segundo archivo de cartera.

4. Ahora, importemos una clase específica del módulo `stock`. En lugar de importar todo el módulo, podemos importar solo la clase `Stock` usando la declaración `from...import`.

```python
from stock import Stock
```

5. Después de importar la clase `Stock`, podemos crear un objeto `Stock`. Un objeto es una instancia de una clase. Crearemos un objeto `Stock` con el nombre `GOOG`, 100 acciones y un precio de `490.10`. Luego imprimiremos el nombre de la acción y calcularemos su costo usando el método `cost()`.

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)
print(s.cost())
```

La salida debe ser:

```
GOOG
49010.0
```

6. Finalmente, cuando hayamos terminado de usar el intérprete de Python, podemos salir de él usando la función `exit()`.

```python
exit()
```

Este laboratorio ha demostrado dos formas diferentes de importar código de Python:

- `import module_name` - Esto importa todo el módulo, haciendo que todas las funciones, clases y variables en ese módulo estén disponibles para su uso.
- `from module_name import specific_item` - Esto importa solo un elemento específico (como una clase o una función) del módulo, lo que puede ser útil si solo necesitas una parte de la funcionalidad del módulo.

# Comprender el acceso a atributos en Python

En Python, los objetos son un concepto fundamental. Pueden almacenar datos en atributos, que son como contenedores con nombre para valores. Puedes pensar en los atributos como variables que pertenecen a un objeto. Hay varias formas de acceder a estos atributos. El método más sencillo y comúnmente utilizado es la notación de punto (`.`). Sin embargo, Python también ofrece funciones específicas que te brindan más flexibilidad al trabajar con atributos.

## La notación de punto

Comencemos creando un objeto `Stock` y veamos cómo podemos manipular sus atributos utilizando la notación de punto. La notación de punto es una forma sencilla e intuitiva de acceder y modificar los atributos de un objeto.

Primero, abre una nueva terminal y inicia la shell interactiva de Python. Aquí es donde puedes escribir y ejecutar código Python línea por línea.

```python
# Open a new terminal and run Python interactive shell
python3

# Import the Stock class from the stock module
from stock import Stock

# Create a Stock object
s = Stock('GOOG', 100, 490.1)

# Get an attribute
print(s.name)    # Output: 'GOOG'

# Set an attribute
s.shares = 50
print(s.shares)  # Output: 50

# Delete an attribute
del s.shares
# If we try to access s.shares now, we'll get an AttributeError
```

En el código anterior, primero importamos la clase `Stock` del módulo `stock`. Luego creamos una instancia de la clase `Stock` llamada `s`. Para obtener el valor del atributo `name`, usamos `s.name`. Para cambiar el valor del atributo `shares`, simplemente asignamos un nuevo valor a `s.shares`. Y si queremos eliminar un atributo, usamos la palabra clave `del` seguida del nombre del atributo.

## Funciones de acceso a atributos

Python proporciona cuatro funciones integradas (built - in functions) que son muy útiles para la manipulación de atributos. Estas funciones te dan más control al trabajar con atributos, especialmente cuando necesitas manejarlos de forma dinámica.

1. `getattr()` - Esta función se utiliza para obtener el valor de un atributo.
2. `setattr()` - Te permite establecer el valor de un atributo.
3. `delattr()` - Puedes usar esta función para eliminar un atributo.
4. `hasattr()` - Esta función verifica si un atributo existe en un objeto.

Veamos cómo usar estas funciones:

```python
# Create a new Stock object
s = Stock('GOOG', 100, 490.1)

# Get an attribute
print(getattr(s, 'name'))       # Output: 'GOOG'

# Set an attribute
setattr(s, 'shares', 50)
print(s.shares)                 # Output: 50

# Check if an attribute exists
print(hasattr(s, 'name'))       # Output: True
print(hasattr(s, 'symbol'))     # Output: False

# Delete an attribute
delattr(s, 'shares')
print(hasattr(s, 'shares'))     # Output: False
```

Estas funciones son especialmente útiles cuando necesitas trabajar con atributos de forma dinámica. En lugar de usar nombres de atributos codificados de forma rígida, puedes usar nombres de variables. Por ejemplo, si tienes una variable que almacena el nombre de un atributo, puedes pasar esa variable a estas funciones para realizar operaciones en el atributo correspondiente. Esto te da más flexibilidad en tu código, especialmente cuando se trata de diferentes objetos y atributos de forma más dinámica.

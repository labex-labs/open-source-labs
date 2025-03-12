# Agregar un método sell a la clase Stock

En este paso, vamos a mejorar la clase `Stock` agregando un nuevo método. Un método es como una función especial que pertenece a una clase y puede trabajar con los objetos creados a partir de esa clase. Crearemos un método llamado `sell(nshares)` que nos ayudará a simular la acción de vender acciones de una empresa. Cuando se venden acciones, la cantidad de acciones que se poseen disminuye, y este método se encargará de esa reducción para nosotros.

## ¿Qué es un método?

Primero, entendamos qué es un método. Un método es una función que se define dentro de una clase. Está diseñado para operar en instancias (que son como copias individuales) de esa clase. Cuando se llama a un método en un objeto, puede acceder a todos los atributos (características) de ese objeto. Lo hace a través del parámetro `self`. El parámetro `self` es una referencia al objeto en el que se está llamando al método. Entonces, cuando se usa `self` dentro de un método, se está refiriendo al objeto específico sobre el que está actuando el método.

## Instrucciones de implementación

1. Primero, necesitamos abrir el archivo `stock.py` en el editor. Para hacer esto, usaremos la línea de comandos. Abra su terminal y ejecute el siguiente comando. Este comando cambia el directorio al directorio `project` donde se encuentra el archivo `stock.py`.

```bash
cd ~/project
```

2. Una vez que tenga abierto el archivo `stock.py`, debe encontrar un comentario específico en la clase `Stock`. Busque el comentario `# TODO: Add sell(nshares) method here`. Este comentario es un marcador que indica dónde debemos agregar nuestro nuevo método `sell`.

3. Ahora, es el momento de agregar el método `sell`. Este método tomará un parámetro llamado `nshares`, que representa la cantidad de acciones que desea vender. El trabajo principal de este método es disminuir el atributo `shares` del objeto `Stock` en la cantidad de acciones que está vendiendo.

Aquí está el código para el método `sell` que debe agregar:

```python
def sell(self, nshares):
    self.shares -= nshares
```

En este código, `self.shares` se refiere al atributo `shares` del objeto `Stock`. El operador `-=` resta el valor de `nshares` del valor actual de `self.shares`.

4. Después de agregar el método `sell`, debe guardar el archivo `stock.py`. Puede hacer esto presionando `Ctrl+S` en su teclado o seleccionando "Archivo > Guardar" desde el menú de su editor.

5. Para asegurarnos de que nuestro método `sell` funcione correctamente, crearemos un script de prueba. Cree un nuevo archivo de Python llamado `test_sell.py` y agregue el siguiente código a él:

```python
# test_sell.py
from stock import Stock

# Create a stock object
s = Stock('GOOG', 100, 490.10)
print(f"Initial shares: {s.shares}")

# Sell 25 shares
s.sell(25)
print(f"Shares after selling: {s.shares}")
```

En este script, primero importamos la clase `Stock` del archivo `stock.py`. Luego creamos un objeto `Stock` llamado `s` con el símbolo de la acción `GOOG`, 100 acciones y un precio de 490.10. Imprimimos la cantidad inicial de acciones. Después de eso, llamamos al método `sell` en el objeto `s` para vender 25 acciones. Finalmente, imprimimos la cantidad de acciones después de la venta.

6. Ahora, ejecutaremos el script de prueba para ver si nuestro método `sell` está funcionando como se espera. Abra su terminal nuevamente y ejecute el siguiente comando:

```bash
python3 test_sell.py
```

Si todo está funcionando correctamente, debería ver una salida similar a esta:

```
Initial shares: 100
Shares after selling: 75
```

Esta salida confirma que nuestro método `sell` está funcionando correctamente. Ha reducido con éxito la cantidad de acciones en la cantidad que especificamos.

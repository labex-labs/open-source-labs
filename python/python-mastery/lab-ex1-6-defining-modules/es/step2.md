# Comprender el módulo principal en Python

En Python, cuando ejecutas un script directamente, este actúa como el módulo "principal". Python tiene una variable especial llamada `__name__`. Cuando se ejecuta un archivo directamente, Python establece el valor de `__name__` en `"__main__"`. Esto es diferente a cuando el archivo se importa como un módulo.

Esta característica es muy útil porque te permite escribir código que se comporta de manera diferente dependiendo de si el archivo se ejecuta directamente o se importa. Por ejemplo, es posible que desees que cierto código se ejecute solo cuando ejecutas el archivo como un script, pero no cuando es importado por otro script.

## Modificar pcost.py para usar el patrón del módulo principal

Modifiquemos el programa `pcost.py` para aprovechar este patrón.

1. Primero, debes abrir el archivo `pcost.py` en el editor. Puedes usar los siguientes comandos para navegar al directorio del proyecto y crear el archivo si no existe:

```bash
cd ~/project
touch pcost.py
```

El comando `cd` cambia el directorio actual al directorio `project` en tu directorio principal. El comando `touch` crea un nuevo archivo llamado `pcost.py` si no existe.

2. Ahora, modifica el archivo `pcost.py` para que se vea así:

```python
# pcost.py

def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                nshares = int(fields[1])
                price = float(fields[2])
                total_cost += nshares * price
            except (ValueError, IndexError):
                print(f"Couldn't parse: {line}")

    return total_cost

# This code only runs when the file is executed as a script
if __name__ == "__main__":
    total = portfolio_cost('portfolio.dat')
    print(total)
```

El cambio principal aquí es que hemos envuelto el código al final en una condición `if __name__ == "__main__":`. Esto significa que el código dentro de este bloque solo se ejecutará cuando el archivo se ejecute directamente como un script, no cuando se importe como un módulo.

3. Después de realizar estos cambios, guarda el archivo y cierra el editor.

## Probar el módulo modificado

Ahora, probemos nuestro módulo modificado de dos maneras diferentes para ver cómo se comporta.

1. Primero, ejecuta el programa directamente como un script usando el siguiente comando:

```bash
python3 pcost.py
```

Debes ver la salida `44671.15`, igual que antes. Esto se debe a que cuando ejecutas el script directamente, la variable `__name__` se establece en `"__main__"`, por lo que el código dentro del bloque `if __name__ == "__main__":` se ejecuta.

2. A continuación, inicia el intérprete de Python nuevamente e importa el módulo:

```bash
python3
```

```python
import pcost
```

Esta vez, no verás ninguna salida. Cuando importas el módulo, la variable `__name__` se establece en `"pcost"` (el nombre del módulo), no en `"__main__"`. Por lo tanto, el código dentro del bloque `if __name__ == "__main__":` no se ejecuta.

3. Para verificar que la función `portfolio_cost` siga funcionando, puedes llamarla así:

```python
pcost.portfolio_cost('portfolio.dat')
```

La función debe devolver `44671.15`, lo que significa que está funcionando correctamente.

4. Finalmente, sal del intérprete de Python usando el siguiente comando:

```python
exit()
```

Este patrón es muy útil cuando se crean archivos de Python que se pueden usar tanto como módulos importables como como scripts independientes. El código dentro del bloque `if __name__ == "__main__":` solo se ejecuta cuando el archivo se ejecuta directamente, no cuando se importa como un módulo.

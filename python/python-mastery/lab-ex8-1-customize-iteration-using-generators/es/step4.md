# Creando un generador para datos en streaming

En programación, los generadores son una herramienta poderosa, especialmente cuando se trata de resolver problemas del mundo real, como monitorear una fuente de datos en streaming. En esta sección, aprenderemos cómo aplicar lo que hemos aprendido sobre generadores a un escenario práctico de este tipo. Vamos a crear un generador que supervise un archivo de registro y nos proporcione las nuevas líneas a medida que se agregan al archivo.

## Configurando la fuente de datos

Antes de comenzar a crear el generador, necesitamos configurar una fuente de datos. En este caso, utilizaremos un programa de simulación que genera datos del mercado de valores.

Primero, debes abrir una nueva terminal en el WebIDE. Aquí es donde ejecutarás los comandos para iniciar la simulación.

Después de abrir la terminal, ejecutarás el programa de simulación de valores. Estos son los comandos que debes ingresar:

```bash
cd ~/project
python3 stocksim.py
```

El primer comando `cd ~/project` cambia el directorio actual al directorio `project` en tu directorio principal. El segundo comando `python3 stocksim.py` ejecuta el programa de simulación de valores. Este programa generará datos del mercado de valores y los escribirá en un archivo llamado `stocklog.csv` en el directorio actual. Deja que este programa se ejecute en segundo plano mientras trabajamos en el código de monitoreo.

## Creando un simple monitor de archivos

Ahora que tenemos configurada nuestra fuente de datos, creemos un programa que supervise el archivo `stocklog.csv`. Este programa mostrará cualquier cambio de precio negativo.

1. Primero, crea un nuevo archivo llamado `follow.py` en el WebIDE. Para hacer esto, debes cambiar el directorio al directorio `project` utilizando el siguiente comando en la terminal:

```bash
cd ~/project
```

2. A continuación, agrega el siguiente código al archivo `follow.py`. Este código abre el archivo `stocklog.csv`, mueve el puntero del archivo al final del archivo y luego verifica continuamente si hay nuevas líneas. Si se encuentra una nueva línea y representa un cambio de precio negativo, imprime el nombre de la acción, el precio y el cambio.

```python
# follow.py
import os
import time

f = open('stocklog.csv')
f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file

while True:
    line = f.readline()
    if line == '':
        time.sleep(0.1)   # Sleep briefly and retry
        continue
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print('%10s %10.2f %10.2f' % (name, price, change))
```

3. Después de agregar el código, guarda el archivo. Luego, ejecuta el programa utilizando el siguiente comando en la terminal:

```bash
python3 follow.py
```

Deberías ver una salida que muestre las acciones con cambios de precio negativos. Podría verse algo así:

```
      AAPL     148.24      -1.76
      GOOG    2498.45      -1.55
```

Si deseas detener el programa, presiona `Ctrl+C` en la terminal.

## Convirtiendo en una función generadora

Si bien el código anterior funciona, podemos hacerlo más reutilizable y modular convirtiéndolo en una función generadora. Una función generadora es un tipo especial de función que se puede pausar y reanudar, y que produce valores uno a la vez.

1. Abre el archivo `follow.py` nuevamente y modifícalo para utilizar una función generadora. Este es el código actualizado:

```python
# follow.py
import os
import time

def follow(filename):
    """
    Generator function that yields new lines in a file as they are added.
    Similar to the 'tail -f' Unix command.
    """
    f = open(filename)
    f.seek(0, os.SEEK_END)   # Move to the end of the file

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)   # Sleep briefly and retry
            continue
        yield line

# Example usage - monitor stocks with negative price changes
if __name__ == '__main__':
    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print('%10s %10.2f %10.2f' % (name, price, change))
```

La función `follow` ahora es una función generadora. Abre el archivo, se mueve al final y luego verifica continuamente si hay nuevas líneas. Cuando se encuentra una nueva línea, la produce.

2. Guarda el archivo y ejecútalo nuevamente utilizando el comando:

```bash
python3 follow.py
```

La salida debe ser la misma que antes. Pero ahora, la lógica de monitoreo de archivos está encapsulada en la función generadora `follow`. Esto significa que podemos reutilizar esta función en otros programas que necesiten monitorear un archivo.

## Entendiendo el poder de los generadores

Al convertir nuestro código de lectura de archivos en una función generadora, lo hemos hecho mucho más flexible y reutilizable. La función `follow()` se puede utilizar en cualquier programa que necesite monitorear un archivo, no solo para datos de valores.

Por ejemplo, podrías utilizarla para monitorear registros de servidores, registros de aplicaciones o cualquier otro archivo que se actualice con el tiempo. Esto muestra cómo los generadores son una excelente manera de manejar fuentes de datos en streaming de forma limpia y modular.

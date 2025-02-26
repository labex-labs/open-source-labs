# Monitoreando una fuente de datos en streaming

Los generadores también pueden ser una forma útil de simplemente producir un flujo de datos. En esta parte, exploraremos esta idea escribiendo un generador para monitorear un archivo de registro. Para comenzar, siga cuidadosamente las siguientes instrucciones.

El programa `stocksim.py` es un programa que simula datos del mercado de valores. Como salida, el programa escribe constantemente datos en tiempo real en un archivo `stocklog.csv`. En una ventana de comando (no IDLE) vaya al directorio `\` y ejecute este programa:

    % python3 stocksim.py

Si está en Windows, simplemente localice el programa `stocksim.py` y haga doble clic en él para ejecutarlo. Ahora, olvídese de este programa (simplemente déjelo en ejecución). Una vez más, simplemente deje que este programa se ejecute en segundo plano: se ejecutará durante varias horas (no debe preocuparse por ello).

Una vez que el programa anterior está en ejecución, escribamos un pequeño programa para abrir el archivo, buscar hasta el final y esperar a la nueva salida. Cree un archivo `follow.py` y ponga este código en él:

```python
# follow.py
import os
import time
f = open('stocklog.csv')
f.seek(0, os.SEEK_END)   # Mueva el puntero del archivo 0 bytes desde el final del archivo

while True:
    line = f.readline()
    if line == '':
        time.sleep(0.1)   # Duerma brevemente y vuelva a intentarlo
        continue
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print('%10s %10.2f %10.2f' % (name, price, change))
```

Si ejecuta el programa, verá un cotizador de valores en tiempo real. En el fondo, este código es como el comando Unix `tail -f` que se utiliza para monitorear un archivo de registro.

**Nota**: El uso del método `readline()` en este ejemplo es un poco inusual en el sentido de que no es la forma habitual de leer líneas de un archivo (normalmente simplemente se utilizaría un `for`-bucle). Sin embargo, en este caso, lo estamos utilizando para examinar repetidamente el final del archivo para ver si se ha agregado más datos (`readline()` devolverá datos nuevos o una cadena vacía).

Si examina el código detenidamente, la primera parte del código está produciendo líneas de datos mientras que las declaraciones al final del bucle `while` están consumiendo los datos. Una característica principal de las funciones generadoras es que se puede mover todo el código de producción de datos a una función reusable.

Modifique el código de modo que la lectura del archivo se realice mediante una función generadora `follow(filename)`. Hágalo de modo que el siguiente código funcione:

```python
>>> for line in follow('stocklog.csv'):
          print(line, end='')

... Debería ver líneas de salida producidas aquí...
```

Modifique el código del cotizador de valores de modo que se vea así:

```python
for line in follow('stocklog.csv'):
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print('%10s %10.2f %10.2f' % (name, price, change))
```

**Discusión**

Algo muy poderoso acaba de suceder aquí. Se ha movido un patrón de iteración interesante (leer líneas al final de un archivo) a su propia pequeña función. La función `follow()` ahora es una utilidad completamente general que se puede utilizar en cualquier programa. Por ejemplo, se podría utilizar para monitorear registros de servidor, registros de depuración y otras fuentes de datos similares. Eso es bastante genial.

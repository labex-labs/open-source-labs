# Ejercicio 6.5: Monitorear una fuente de datos en streaming

Los generadores pueden ser una manera interesante de monitorear fuentes de datos en tiempo real, como archivos de registro o flujos de mercado de valores. En esta parte, exploraremos esta idea. Para comenzar, siga detenidamente las siguientes instrucciones.

El programa `stocksim.py` es un programa que simula datos del mercado de valores. Como salida, el programa escribe constantemente datos en tiempo real en un archivo `stocklog.csv`. En una ventana de comando separada, vaya al directorio correspondiente y ejecute este programa:

```bash
$ python3 stocksim.py
```

Si está en Windows, simplemente localice el programa `stocksim.py` y haga doble clic en él para ejecutarlo. Ahora, olvide este programa (simplemente déjelo en ejecución). Usando otra ventana, vea el archivo `stocklog.csv` que está siendo escrito por el simulador. Debería ver nuevas líneas de texto agregadas al archivo cada pocos segundos. Una vez más, simplemente déjelo ejecutar en segundo plano: se ejecutará durante varias horas (no debe preocuparse por ello).

Una vez que el programa anterior está en ejecución, escribamos un pequeño programa para abrir el archivo, buscar hasta el final y esperar a nuevos datos. Cree un archivo `follow.py` y ponga este código en él:

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
        print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```

Si ejecuta el programa, verá un cotizador de valores en tiempo real. En el fondo, este código es similar al comando Unix `tail -f` que se utiliza para monitorear un archivo de registro.

Nota: El uso del método `readline()` en este ejemplo es un poco inusual en el sentido de que no es la forma habitual de leer líneas de un archivo (normalmente se usaría un bucle `for`). Sin embargo, en este caso, lo estamos usando para examinar repetidamente el final del archivo para ver si se han agregado más datos (`readline()` devolverá ya sea nuevos datos o una cadena vacía).

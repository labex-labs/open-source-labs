# Un poco de arte generativo

Cree el siguiente programa y guárdelo en un archivo llamado `art.py`:

```python
# art.py

import sys
import random

chars = '\|/'

def draw(rows, columns):
    for r in range(rows):
        print(''.join(random.choice(chars) for _ in range(columns)))

if __name__ == '__main__':
    if len(sys.argv)!= 3:
        raise SystemExit("Usage: art.py rows columns")
    draw(int(sys.argv[1]), int(sys.argv[2]))
```

Asegúrese de que pueda ejecutar este programa desde la línea de comandos o una terminal.

```bash
python3 art.py 10 20
```

Si ejecuta el comando anterior, obtendrá un mensaje de error y traza. Vaya a corregir el problema y ejecute el programa nuevamente. Debería obtener una salida como esta:

```bash
python3 art.py 10 20
||||/\||//\//\|||\|\
///||\/||\//|\\|\\/\
|\////|//|||\//|/\||
|//\||\/|\///|\|\|/|
|/|//|/|/|\\/\/\||//
|\/\|\//\\//\|\||\\/
|||\\\\/\\\|/||||\/|
\\||\\\|\||||////\\|
//\//|/|\\|\//\|||\/
\\\|/\\|/|\\\|/|/\/|
```

## Nota importante

Es absolutamente esencial que sea capaz de editar, ejecutar y depurar programas de Python normales para el resto de este curso. La elección del editor, IDE o sistema operativo no importa siempre y cuando sea capaz de experimentar de manera interactiva y crear archivos fuente de Python normales que puedan ejecutarse desde la línea de comandos.

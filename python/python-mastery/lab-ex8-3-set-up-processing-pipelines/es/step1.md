# Un ejemplo de corrutina

Empezar a trabajar con corrutinas puede resultar un poco complicado. Aquí hay un programa de ejemplo que realiza la misma tarea que el Ejercicio 8.2, pero con corrutinas. Toma este programa y cópielo en un archivo llamado `cofollow.py`.

```python
# cofollow.py
import os
import time

# Fuente de datos
def follow(filename,target):
    with open(filename,'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
            line = f.readline()
            if line!= '':
                target.send(line)
            else:
                time.sleep(0.1)

# Decorador para funciones de corrutina
from functools import wraps

def consumer(func):
    @wraps(func)
    def start(*args,**kwargs):
        f = func(*args,**kwargs)
        f.send(None)
        return f
    return start

# Corrutina de ejemplo
@consumer
def printer():
    while True:
        item = yield     # Recibe un elemento enviado a mí
        print(item)

# Uso de ejemplo
if __name__ == '__main__':
    follow('stocklog.csv',printer())
```

Ejecuta este programa y asegúrate de que produzca salida. Asegúrate de entender cómo se enlazan las diferentes partes.

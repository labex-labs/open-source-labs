# Entornos virtuales

Una solución común a los problemas de instalación de paquetes es crear un llamado "entorno virtual" para ti mismo. Naturalmente, no existe "un solo modo" de hacerlo: de hecho, hay varias herramientas y técnicas en competencia. Sin embargo, si estás utilizando una instalación estándar de Python, puedes intentar escribir esto:

```bash
$ sudo apt install python3-venv
$ python -m venv mypython
bash %
```

Después de esperar un momento, tendrás un nuevo directorio `mypython` que es tu propia pequeña instalación de Python. Dentro de ese directorio encontrarás un directorio `bin/` (Unix) o un directorio `Scripts/` (Windows). Si ejecutas el script `activate` que se encuentra allí, "activará" esta versión de Python, convirtiéndola en el comando `python` predeterminado para el shell. Por ejemplo:

```bash
$ source mypython/bin/activate
(mypython) bash %
```

A partir de aquí, ahora puedes comenzar a instalar paquetes de Python para ti mismo. Por ejemplo:

    (mypython) $ python -m pip install pandas

...

Para fines de experimentación y prueba de diferentes paquetes, un entorno virtual generalmente funcionará bien. Por otro lado, si estás creando una aplicación y tiene dependencias específicas de paquetes, ese es un problema ligeramente diferente.

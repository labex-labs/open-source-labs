# Estructura de la Aplicación

La organización del código y la estructura de archivos son clave para la mantenibilidad de una aplicación.

No existe un enfoque "uno para todos" para Python. Sin embargo, una estructura que funciona para muchos problemas es la siguiente.

```code
porty-app/
  README.txt
  script.py         # SCRIPT
  porty/
    # CÓDIGO DE LIBRERÍA
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

El nivel superior `porty-app` es un contenedor para todo lo demás: documentación, scripts de nivel superior, ejemplos, etc.

Una vez más, los scripts de nivel superior (si los hay) deben existir fuera del paquete de código. Un nivel arriba.

```python
#!/usr/bin/env python3
# porty-app/script.py
import sys
import porty

porty.report.main(sys.argv)
```

En este momento, tienes un directorio con varios programas:

    pcost.py          # Calcula el costo de la cartera
    report.py         # Genera un informe
    ticker.py         # Produce un cotizador de acciones en tiempo real

Hay una variedad de módulos de soporte con otras funcionalidades:

    stock.py          # Clase Stock
    portfolio.py      # Clase Portfolio
    fileparse.py      # Análisis de CSV
    tableformat.py    # Tablas formateadas
    follow.py         # Sigue un archivo de registro
    typedproperty.py  # Propiedades de clase tipadas

En este ejercicio, vamos a limpiar el código y ponerlo en un paquete común.

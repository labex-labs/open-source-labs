# Paquetes vs Módulos

Para colecciones más grandes de código, es común organizar los módulos en un paquete.

```code
# De esto
pcost.py
report.py
fileparse.py

# A esto
porty/
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

Elegís un nombre y creáis un directorio de nivel superior. `porty` en el ejemplo anterior (claramente, elegir este nombre es el primer paso más importante).

Agregá un archivo `__init__.py` al directorio. Puede estar vacío.

Colocá tus archivos fuente en el directorio.

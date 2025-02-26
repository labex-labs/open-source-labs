# Ruta de búsqueda de módulos

Como se ha señalado, `sys.path` contiene las rutas de búsqueda. Puedes ajustarlas manualmente si es necesario.

```python
import sys
sys.path.append('/project/foo/pyfiles')
```

También se pueden agregar rutas a través de variables de entorno.

```python
% env PYTHONPATH=/project/foo/pyfiles python3
Python 3.6.0 (predeterminado, 3 feb 2017, 05:53:21)
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.38)]
>>> import sys
>>> sys.path
['','/project/foo/pyfiles',...]
```

En general, no debería ser necesario ajustar manualmente la ruta de búsqueda de módulos. Sin embargo, a veces puede surgir si intentas importar código de Python que se encuentra en una ubicación inusual o no es fácilmente accesible desde el directorio de trabajo actual.

Para este ejercicio que involucra módulos, es fundamental asegurarse de que estás ejecutando Python en un entorno adecuado. Los módulos a menudo presentan a los nuevos programadores problemas relacionados con el directorio de trabajo actual o con la configuración de la ruta de Python. Para este curso, se asume que estás escribiendo todo tu código en el directorio `~/project`. Para obtener los mejores resultados, debes asegurarte de que también estés en ese directorio cuando lanzas el intérprete. Si no es así, debes asegurarte de que `~/project` se agregue a `sys.path`.

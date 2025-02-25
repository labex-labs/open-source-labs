# Establecer la ruta de la fuente

Establecemos la ruta de la fuente utilizando el método `mpl.get_data_path()` para obtener la ruta del directorio de datos y luego agregamos la ruta del archivo de fuente `cmr10.ttf` a ella utilizando el método `Path()` del módulo `pathlib`.

```python
from pathlib import Path

fpath = Path(mpl.get_data_path(), "fonts/ttf/cmr10.ttf")
```

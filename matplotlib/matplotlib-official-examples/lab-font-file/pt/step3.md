# Definir o caminho da fonte

Definimos o caminho da fonte usando o método `mpl.get_data_path()` para obter o caminho do diretório de dados e, em seguida, anexamos o caminho do arquivo de fonte `cmr10.ttf` a ele usando o método `Path()` do módulo `pathlib`.

```python
from pathlib import Path

fpath = Path(mpl.get_data_path(), "fonts/ttf/cmr10.ttf")
```

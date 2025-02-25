# Spécifiez le chemin de la police

Nous spécifions le chemin de la police en utilisant la méthode `mpl.get_data_path()` pour obtenir le chemin du répertoire de données, puis en ajoutant le chemin du fichier de police `cmr10.ttf` à l'aide de la méthode `Path()` du module `pathlib`.

```python
from pathlib import Path

fpath = Path(mpl.get_data_path(), "fonts/ttf/cmr10.ttf")
```

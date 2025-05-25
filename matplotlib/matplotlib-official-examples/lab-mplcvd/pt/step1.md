# Importar as bibliotecas e módulos necessários

Primeiramente, precisamos importar as bibliotecas e módulos necessários, incluindo Matplotlib, NumPy e colorspacious. Também definimos as opções de filtro de cores que queremos simular.

```python
import functools
from pathlib import Path

import colorspacious

import numpy as np

_BUTTON_NAME = "Filter"
_BUTTON_HELP = "Simulate color vision deficiencies"
_MENU_ENTRIES = {
    "None": None,
    "Greyscale": "greyscale",
    "Deuteranopia": "deuteranomaly",
    "Protanopia": "protanomaly",
    "Tritanopia": "tritanomaly",
}
```

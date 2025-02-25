# Importar las bibliotecas y módulos necesarios

En primer lugar, necesitamos importar las bibliotecas y módulos necesarios, incluyendo Matplotlib, NumPy y colorspacious. También establecemos las opciones de filtro de color que queremos simular.

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

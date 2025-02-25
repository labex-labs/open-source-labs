# Importieren der erforderlichen Bibliotheken und Module

Zunächst müssen wir die erforderlichen Bibliotheken und Module importieren, einschließlich Matplotlib, NumPy und colorspacious. Wir legen auch die Farbfilteroptionen fest, die wir simulieren möchten.

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

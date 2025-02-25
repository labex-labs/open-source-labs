# Abhängigkeiten importieren

In diesem Schritt importieren wir die erforderlichen Abhängigkeiten. Wir werden `base64` verwenden, um die Bilddaten zu kodieren, `BytesIO`, um die Bilddaten im Speicher zu speichern, `Flask`, um den Webanwendungsserver zu erstellen, und `Figure`, um die Figuren zu erstellen.

```python
import base64
from io import BytesIO

from flask import Flask

from matplotlib.figure import Figure
```

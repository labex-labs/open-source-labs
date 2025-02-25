# Startoptionen setzen

Wir können ein Startskript im Python/IPython-Umgebung erstellen, um pandas zu importieren und Optionen zu setzen, was das Arbeiten mit pandas effizienter macht.

```python
# This is an example of a startup script
# Place this in a.py file in the startup directory of IPython profile
import pandas as pd

pd.set_option("display.max_rows", 999)
pd.set_option("display.precision", 5)
```

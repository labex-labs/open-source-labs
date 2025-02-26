# Bemerkungen zum Importieren

Variationen beim Importieren _ändern_ die Art und Weise, wie Module funktionieren, _nicht_.

```python
import math
# vs
import math as m
# vs
from math import cos, sin
...
```

Insbesondere führt `import` immer die _gesamte_ Datei aus und Module bleiben immer noch isolierte Umgebungen.

Die `import modul as`-Anweisung ändert nur den Namen lokal. Die `from math import cos, sin`-Anweisung lädt hinter den Kulissen immer noch das gesamte math-Modul. Es kopiert lediglich die `cos`- und `sin`-Namen aus dem Modul in den lokalen Namensraum, nachdem es fertig ist.

# Extrahieren des Renderer-Puffers zu einem numpy-Array

Die zweite Option, um den Plot zu speichern, besteht darin, den Renderer-Puffer in ein numpy-Array zu extrahieren. Dies ermöglicht es uns, Matplotlib innerhalb eines CGI-Skripts zu verwenden, ohne dass wir ein Diagramm auf die Festplatte schreiben müssen. In diesem Beispiel extrahieren wir den Renderer-Puffer und konvertieren ihn in ein numpy-Array.

```python
import numpy as np

canvas.draw()
rgba = np.asarray(canvas.buffer_rgba())
```

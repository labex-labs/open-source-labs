# Importieren von Bilddaten

Um zu beginnen, müssen wir die erforderlichen Bibliotheken importieren und die Bilddaten in ein NumPy-Array laden. Im unserem Fall werden wir die `PIL`-Bibliothek verwenden, um das Bild zu laden und es dann in ein NumPy-Array zu konvertieren.

```python
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = np.asarray(Image.open('./stinkbug.png'))
```
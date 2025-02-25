# Bibliotheken importieren und Box-Stile erhalten

In diesem Schritt werden wir die erforderlichen Bibliotheken importieren und die Box-Stile erhalten, die wir für das Plotten verwenden werden.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
from matplotlib.patches import FancyBboxPatch
import matplotlib.transforms as mtransforms
import inspect

styles = mpatch.BoxStyle.get_styles()
```

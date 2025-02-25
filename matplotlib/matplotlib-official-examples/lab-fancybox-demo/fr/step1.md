# Importez les bibliothèques et obtenez les styles de boîte

Dans cette étape, nous allons importer les bibliothèques nécessaires et obtenir les styles de boîte que nous utiliserons pour tracer.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
from matplotlib.patches import FancyBboxPatch
import matplotlib.transforms as mtransforms
import inspect

styles = mpatch.BoxStyle.get_styles()
```

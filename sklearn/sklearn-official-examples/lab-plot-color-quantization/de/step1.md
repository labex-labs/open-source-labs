# Originalbild laden und anzeigen

Wir beginnen mit dem Laden und Anzeigen des Originalbilds des Sommerpalaasts.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_sample_image

# Lade das Sommerpalast-Foto
china = load_sample_image("china.jpg")

# Zeige das Originalbild an
plt.figure()
plt.axis("off")
plt.title("Originalbild")
plt.imshow(china)
plt.show()
```

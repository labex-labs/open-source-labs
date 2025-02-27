# Charger et afficher l'image d'origine

Nous allons commencer par charger et afficher l'image d'origine du Palais d'été.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_sample_image

# Charger la photo du Palais d'été
china = load_sample_image("china.jpg")

# Afficher l'image d'origine
plt.figure()
plt.axis("off")
plt.title("Image d'origine")
plt.imshow(china)
plt.show()
```

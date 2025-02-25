# Préparation

Avant de commencer, nous devons nous assurer que Matplotlib est installé. Vous pouvez l'installer à l'aide de pip, en exécutant la commande suivante :

```python
!pip install matplotlib
```

Une fois installé, nous devons importer la bibliothèque et configurer l'environnement :

```python
import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# Create new Figure with black background
fig = plt.figure(figsize=(8, 8), facecolor='black')

# Add a subplot with no frame
ax = plt.subplot(frameon=False)
```

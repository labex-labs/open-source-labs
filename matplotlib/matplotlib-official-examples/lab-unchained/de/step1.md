# Einrichtung

Bevor wir beginnen, müssen wir sicherstellen, dass Matplotlib installiert ist. Sie können es mit pip installieren, indem Sie den folgenden Befehl ausführen:

```python
!pip install matplotlib
```

Nach der Installation müssen wir die Bibliothek importieren und die Umgebung einrichten:

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

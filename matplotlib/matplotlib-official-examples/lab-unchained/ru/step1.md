# Настройка

Прежде чем мы начнем, необходимо убедиться, что Matplotlib установлен. Его можно установить с помощью pip, выполнив следующую команду:

```python
!pip install matplotlib
```

После установки необходимо импортировать библиотеку и настроить окружение:

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

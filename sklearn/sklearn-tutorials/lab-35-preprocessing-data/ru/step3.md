# Нормализация

Нормализация - это процесс масштабирования отдельных образцов так, чтобы они имели единичную норму. Она обычно используется, когда величина данных не имеет значения, и нас интересует только направление (или угол) данных. Мы можем использовать `Normalizer` из scikit-learn для выполнения нормализации.

```python
from sklearn.preprocessing import Normalizer
import numpy as np

# Create a sample dataset
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# Initialize the Normalizer
normalizer = Normalizer()

# Fit and transform the training data
X_normalized = normalizer.fit_transform(X)

# Print the transformed data
print(X_normalized)
```

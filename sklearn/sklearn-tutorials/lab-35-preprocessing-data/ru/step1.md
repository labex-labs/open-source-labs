# Стандартизация

Стандартизация является распространенным этапом предварительной обработки для многих алгоритмов машинного обучения. Она преобразует признаки так, чтобы они имели нулевое среднее значение и единичную дисперсию. Мы можем использовать `StandardScaler` из scikit-learn для выполнения стандартизации.

```python
from sklearn.preprocessing import StandardScaler
import numpy as np

# Create a sample dataset
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit the scaler on the training data
scaler.fit(X)

# Transform the training data
X_scaled = scaler.transform(X)

# Print the transformed data
print(X_scaled)
```

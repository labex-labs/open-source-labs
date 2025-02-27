# Подготовка набора данных для машинного обучения

Прежде чем мы сможем обучить модель машинного обучения на наборе данных, нам нужно подготовить данные, разделив их на обучающий и тестовый наборы. Мы можем сделать это с использованием функции `train_test_split` из scikit - learn:

```python
from sklearn.model_selection import train_test_split

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)
```

# Загрузка датасета

Во - первых, нам нужно загрузить датасет, который мы можем использовать для обучения нашей прогнозной модели. Мы будем использовать датасет Diabetes из scikit - learn, который содержит информацию о пациентах с диабетом.

```python
from sklearn.datasets import load_diabetes

# Load the Diabetes dataset
диабет = load_diabetes()

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(диабет.data, диабет.target, random_state = 0)
```

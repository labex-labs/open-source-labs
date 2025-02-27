# Загружаем и предобрабатываем данные

Далее мы загрузим датасет iris и предобработаем его, масштабируя признаки с использованием StandardScaler.

```python
# Load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
```

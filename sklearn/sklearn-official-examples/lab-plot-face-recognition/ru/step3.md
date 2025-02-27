# Предварительная обработка данных

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

Мы разбиваем набор данных на обучающую и тестовую выборки и выполняем предварительную обработку данных, масштабируя входные данные с помощью функции `StandardScaler()`.

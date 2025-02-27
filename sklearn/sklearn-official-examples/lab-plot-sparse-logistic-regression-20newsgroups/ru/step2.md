# Загрузка и подготовка данных

Далее мы загружаем набор данных `20newsgroups` и готовим данные для обучения и тестирования.

```python
# Мы используем решатель SAGA
solver = "saga"

# Уменьшите значение для более быстрого выполнения
n_samples = 5000

X, y = fetch_20newsgroups_vectorized(subset="all", return_X_y=True)
X = X[:n_samples]
y = y[:n_samples]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state=42, stratify=y, test_size=0.1
)
train_samples, n_features = X_train.shape
n_classes = np.unique(y).shape[0]

print(
    "Dataset 20newsgroup, train_samples=%i, n_features=%i, n_classes=%i"
    % (train_samples, n_features, n_classes)
)
```

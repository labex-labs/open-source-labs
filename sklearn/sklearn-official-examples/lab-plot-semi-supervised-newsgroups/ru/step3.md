# Обучение и оценка supervised модели

На этом шаге мы разделим набор данных на обучающую и тестовую выборки, а затем обучим и оценим supervised модель, созданную на шаге 2.

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

# Разделение набора данных на обучающую и тестовую выборки
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Обучение и оценка supervised модели
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(
    "Micro-averaged F1 score on test set: %0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```

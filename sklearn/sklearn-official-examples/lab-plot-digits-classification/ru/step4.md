# Разделение набора данных

Мы разделим набор данных на обучающую и тестовую подмножества в соотношении 50% - 50% с использованием метода `train_test_split()` из `sklearn.model_selection`.

```python
X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False
)
```

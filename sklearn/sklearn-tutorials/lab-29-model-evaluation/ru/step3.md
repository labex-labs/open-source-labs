# Функции метрик

Модуль `metrics` библиотеки scikit-learn реализует несколько функций для оценки ошибки предсказания для конкретных целей. Эти функции можно использовать для вычисления качества предсказаний, сделанных моделью.

Вот пример использования функции `accuracy_score` из модуля `metrics`:

```python
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = LogisticRegression()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```

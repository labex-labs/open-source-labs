# Мультиклассовая классификация

#### Описание задачи

Мультиклассовая классификация - это задача классификации с более чем двумя классами. Каждый образец принадлежит только одному классу.

#### Формат целевых переменных

Допустимым представлением целевых переменных для мультиклассовой классификации является одномерный или столбцовый вектор, содержащий более двух дискретных значений.

#### Пример

Рассмотрим датасет Iris для демонстрации мультиклассовой классификации:

```python
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

# Загрузка датасета Iris
X, y = datasets.load_iris(return_X_y=True)

# Обучение логистической регрессии с использованием OneVsRestClassifier
model = OneVsRestClassifier(LogisticRegression())
model.fit(X, y)

# Предсказание классов
predictions = model.predict(X)
print(predictions)
```

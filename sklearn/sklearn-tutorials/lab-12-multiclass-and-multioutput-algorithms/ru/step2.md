# Мультиметкажная классификация

#### Описание задачи

Мультиметкажная классификация - это задача классификации, в которой каждый образец может быть присвоен нескольким меткам. Количество меток, которое может иметь каждый образец, больше двух.

#### Формат целевых переменных

Допустимым представлением целевых переменных для мультиметкажной классификации является бинарная матрица, где каждая строка представляет собой образец, а каждый столбец - класс. Значение 1 указывает на присутствие метки в образце, а 0 или -1 - на ее отсутствие.

#### Пример

Создадим задачу мультиметкажной классификации с использованием функции make_classification:

```python
from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier

# Сгенерируем задачу мультиметкажной классификации
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, random_state=0)
y = y.reshape(-1, 1)

# Обучим мультивыходный классификатор на основе случайного леса
model = MultiOutputClassifier(RandomForestClassifier())
model.fit(X, y)

# Предскажем метки
predictions = model.predict(X)
print(predictions)
```

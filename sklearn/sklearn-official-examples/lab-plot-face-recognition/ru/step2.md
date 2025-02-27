# Загрузка и исследование набора данных

```python
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
n_samples, h, w = lfw_people.images.shape
X = lfw_people.data
n_features = X.shape[1]
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]
```

Мы загружаем набор данных с помощью функции `fetch_lfw_people()` из библиотеки scikit-learn. Затем мы исследуем набор данных, получая количество образцов, высоту и ширину изображений. Мы также получаем входные данные `X`, целевую переменную `y`, имена классов `target_names` и количество классов `n_classes`.

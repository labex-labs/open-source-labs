# Загрузка или генерация небольших наборов данных

Теперь нам нужно загрузить или сгенерировать небольшие наборы данных, которые мы будем использовать в этом примере. Мы будем использовать набор данных ирисов (iris dataset), набор данных с рукописными цифрами (digits dataset) и два набора данных, сгенерированных с использованием функций `make_circles` и `make_moons`.

```python
iris = datasets.load_iris()
X_digits, y_digits = datasets.load_digits(return_X_y=True)
data_sets = [
    (iris.data, iris.target),
    (X_digits, y_digits),
    datasets.make_circles(noise=0.2, factor=0.5, random_state=1),
    datasets.make_moons(noise=0.3, random_state=0),
]
```

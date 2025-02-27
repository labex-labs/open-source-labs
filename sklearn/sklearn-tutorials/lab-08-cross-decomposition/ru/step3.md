# PLSRegression

#### Настраиваем модель PLSRegression

Начнем с алгоритма `PLSRegression`, который представляет собой форму регуляризованной линейной регрессии. Настроим модель на наших данных.

```python
pls = PLSRegression(n_components=2)
pls.fit(X, Y)
```

#### Преобразуем данные

Мы можем преобразовать исходные данные с использованием настроенной модели. Преобразованные данные будут иметь уменьшенную размерность.

```python
X_transformed = pls.transform(X)
Y_transformed = pls.transform(Y)
```

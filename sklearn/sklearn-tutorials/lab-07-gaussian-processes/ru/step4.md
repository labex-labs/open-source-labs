# Примеры GPC

Вероятностные прогнозы с использованием GPC: Этот пример иллюстрирует предсказанные вероятности GPC при различных выборах гиперпараметров.

```python
# Создаем модель GPC с ядром RBF
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# Подгоняем модель под обучающие данные
model.fit(X_train, y_train)

# Предсказываем вероятности классов для тестовых данных
y_prob = model.predict_proba(X_test)
```

Иллюстрация GPC на наборе данных XOR: Этот пример демонстрирует применение GPC на наборе данных XOR. Мы сравниваем результаты использования стационарного, изотропного ядра (RBF) и нестационарного ядра (DotProduct).

```python
# Создаем модели GPC с разными ядрами
isotropic_kernel = RBF(length_scale=1.0)
non_stationary_kernel = DotProduct(sigma_0=1.0)

# Подгоняем модели под набор данных XOR
isotropic_model = GaussianProcessClassifier(kernel=isotropic_kernel)
non_stationary_model = GaussianProcessClassifier(kernel=non_stationary_kernel)
isotropic_model.fit(X_xor, y_xor)
non_stationary_model.fit(X_xor, y_xor)

# Предсказываем с использованием обученных моделей
isotropic_y_pred = isotropic_model.predict(X_test)
non_stationary_y_pred = non_stationary_model.predict(X_test)
```

GPC на наборе данных iris: Этот пример иллюстрирует GPC на наборе данных iris с использованием изотропного ядра RBF и анизотропного ядра RBF. Показано, как различные выборы гиперпараметров могут повлиять на предсказанные вероятности.

```python
# Создаем модели GPC с разными ядрами и подгоняем их под набор данных iris
isotropic_kernel = RBF(length_scale=1.0)
anisotropic_kernel = RBF(length_scale=[1.0, 2.0])
isotropic_model = GaussianProcessClassifier(kernel=isotropic_kernel)
anisotropic_model = GaussianProcessClassifier(kernel=anisotropic_kernel)
isotropic_model.fit(X_train, y_train)
anisotropic_model.fit(X_train, y_train)

# Предсказываем вероятности классов
isotropic_y_prob = isotropic_model.predict_proba(X_test)
anisotropic_y_prob = anisotropic_model.predict_proba(X_test)
```

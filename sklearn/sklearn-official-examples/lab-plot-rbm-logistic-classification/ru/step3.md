# Обучение

В этом шаге мы обучаем модель конвейера, определённую на предыдущем шаге. Мы настраиваем гиперпараметры модели (скорость обучения, размер скрытого слоя, регуляризация), а затем подгоняем обучающие данные под модель.

```python
from sklearn.base import clone

# Hyper-parameters. These were set by cross-validation,
# using a GridSearchCV. Here we are not performing cross-validation to
# save time.
rbm.learning_rate = 0.06
rbm.n_iter = 10

# More components tend to give better prediction performance, but larger
# fitting time
rbm.n_components = 100
logistic.C = 6000

# Training RBM-Logistic Pipeline
rbm_features_classifier.fit(X_train, Y_train)
```

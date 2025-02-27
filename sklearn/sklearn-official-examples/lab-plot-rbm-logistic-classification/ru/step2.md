# Определение модели

В этом шаге мы определяем конвейер классификации с использованием экстрактора признаков BernoulliRBM и логистической регрессионной классификатором. Мы используем классы `BernoulliRBM` и `LogisticRegression` из модулей `sklearn.neural_network` и `sklearn.linear_model` соответственно. Затем мы создаём объект конвейера `rbm_features_classifier`, чтобы объединить два модели.

```python
from sklearn import linear_model
from sklearn.neural_network import BernoulliRBM
from sklearn.pipeline import Pipeline

logistic = linear_model.LogisticRegression(solver="newton-cg", tol=1)
rbm = BernoulliRBM(random_state=0, verbose=True)

rbm_features_classifier = Pipeline(steps=[("rbm", rbm), ("logistic", logistic)])
```

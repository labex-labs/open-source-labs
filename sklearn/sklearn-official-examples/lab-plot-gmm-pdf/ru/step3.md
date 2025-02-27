# Подгонка модели смеси гауссов

Теперь мы подгоним GMM к датасету с использованием класса GaussianMixture из scikit-learn. Зададим количество компонентов равным 2 и тип ковариации "full".

```python
# подгоняем модель смеси гауссов с двумя компонентами
clf = mixture.GaussianMixture(n_components=2, covariance_type="full")
clf.fit(X_train)
```

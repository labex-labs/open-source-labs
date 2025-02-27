# Вычисление коэффициентов Bayesian Ridge с использованием GridSearch

```python
cv = KFold(2)  # генератор кросс-валидации для выбора модели
ridge = BayesianRidge()
cachedir = tempfile.mkdtemp()
mem = Memory(location=cachedir, verbose=1)
```

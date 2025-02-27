# Аппроксимация ядра с добавленным квадратом хи-квадрат (ACS)

Ядро ACS - это ядро на гистограммах, широко используемое в компьютерном зрении. Класс AdditiveChi2Sampler предоставляет приближенное отображение для этого ядра.

Для использования AdditiveChi2Sampler для аппроксимации ядра следуйте шагам:

1. Инициализируйте объект AdditiveChi2Sampler с желаемым количеством выборок (n) и параметром регуляризации (c).

```python
from sklearn.kernel_approximation import AdditiveChi2Sampler

n_samples = 1000
c = 1.0
additive_chi2_sampler = AdditiveChi2Sampler(n_samples=n_samples, sample_steps=2, sample_interval=2, sample_octave=2, c=c)
```

2. Обучите объект AdditiveChi2Sampler на своих тренировочных данных.

```python
additive_chi2_sampler.fit(X_train)
```

3. Преобразуйте свои тренировочные и тестовые данные с использованием объекта AdditiveChi2Sampler.

```python
X_train_transformed = additive_chi2_sampler.transform(X_train)
X_test_transformed = additive_chi2_sampler.transform(X_test)
```

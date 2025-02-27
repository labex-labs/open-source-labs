# Аппроксимация ядра с отклонённым квадратом хи-квадрат (SCS)

Ядро SCS - это вариант возведённого в степень квадрата хи-квадрат ядра, которое позволяет получить простую приближённую оценку с использованием метода Монте-Карло для карты признаков. Класс SkewedChi2Sampler предоставляет приближенное отображение для этого ядра.

Для использования SkewedChi2Sampler для аппроксимации ядра следуйте шагам:

1. Инициализируйте объект SkewedChi2Sampler с желаемым количеством выборок (n) и параметром регуляризации (c).

```python
from sklearn.kernel_approximation import SkewedChi2Sampler

n_samples = 1000
c = 1.0
skewed_chi2_sampler = SkewedChi2Sampler(n_samples=n_samples, sample_steps=2, sample_interval=2, sample_octave=1, c=c)
```

2. Обучите объект SkewedChi2Sampler на своих тренировочных данных.

```python
skewed_chi2_sampler.fit(X_train)
```

3. Преобразуйте свои тренировочные и тестовые данные с использованием объекта SkewedChi2Sampler.

```python
X_train_transformed = skewed_chi2_sampler.transform(X_train)
X_test_transformed = skewed_chi2_sampler.transform(X_test)
```

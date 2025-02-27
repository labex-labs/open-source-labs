# Создание соответствующего ядра

Для создания ядра, которое будет использоваться в гауссовом процессе, мы можем сделать некоторые предположения относительно имеющихся у нас данных. Мы замечаем, что они обладают несколькими характеристиками: есть долгосрочный восходящий тренд, выраженная сезонная вариация и некоторые более мелкие нерегулярности. Мы можем использовать разные подходящие ядра, которые будут учитывать эти особенности.

```python
from sklearn.gaussian_process.kernels import RBF, ExpSineSquared, RationalQuadratic, WhiteKernel

long_term_trend_kernel = 50.0**2 * RBF(length_scale=50.0)
seasonal_kernel = (
    2.0**2
    * RBF(length_scale=100.0)
    * ExpSineSquared(length_scale=1.0, periodicity=1.0, periodicity_bounds="fixed")
)
irregularities_kernel = 0.5**2 * RationalQuadratic(length_scale=1.0, alpha=1.0)
noise_kernel = 0.1**2 * RBF(length_scale=0.1) + WhiteKernel(
    noise_level=0.1**2, noise_level_bounds=(1e-5, 1e5)
)

co2_kernel = (
    long_term_trend_kernel + seasonal_kernel + irregularities_kernel + noise_kernel
)
```

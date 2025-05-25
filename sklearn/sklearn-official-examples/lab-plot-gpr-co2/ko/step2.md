# 적절한 커널 설계

가우시안 프로세스에 사용할 커널을 설계하기 위해, 현재 데이터에 대한 몇 가지 가정을 할 수 있습니다. 데이터는 장기적인 상승 추세, 두드러진 계절적 변동, 그리고 일부 작은 불규칙성을 가지고 있는 것을 관찰할 수 있습니다. 이러한 특징을 포착하는 데 적합한 서로 다른 커널을 사용할 수 있습니다.

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

# 適切なカーネルを設計する

ガウス過程で使用するカーネルを設計するには、手元のデータに関するいくつかの仮定を立てることができます。それらはいくつかの特徴を持っていることがわかります。長期的な上昇傾向、顕著な季節変動、そしていくつかの小さな不規則性があります。これらの特徴を捉えるために、異なる適切なカーネルを使用することができます。

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

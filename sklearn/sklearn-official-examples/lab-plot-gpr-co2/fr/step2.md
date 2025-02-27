# Construire le noyau approprié

Pour concevoir le noyau à utiliser avec notre processus gaussien, nous pouvons faire quelques hypothèses concernant les données disponibles. Nous observons qu'elles présentent plusieurs caractéristiques : une tendance à la hausse à long terme, une variation saisonnière prononcée et quelques irrégularités plus petites. Nous pouvons utiliser différents noyaux appropriés qui captureront ces caractéristiques.

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

# Diseñar el kernel adecuado

Para diseñar el kernel que se utilizará con nuestro proceso gaussiano, podemos hacer algunos supuestos sobre los datos que tenemos a mano. Observamos que tienen varias características: vemos una tendencia ascendente a largo plazo, una variación estacional pronunciada y algunas irregularidades menores. Podemos utilizar diferentes kernels adecuados que capturen estas características.

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

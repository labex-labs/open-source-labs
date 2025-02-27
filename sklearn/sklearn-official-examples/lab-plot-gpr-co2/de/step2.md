# Den passenden Kernel entwerfen

Um den Kernel zu entwerfen, der mit unserem Gaussian-Prozess verwendet werden soll, können wir einige Annahmen über die vorhandenen Daten machen. Wir stellen fest, dass sie mehrere Merkmale aufweisen: einen langfristigen Anstiegstrend, eine ausgeprägte saisonale Schwankung und einige kleinere Unregelmäßigkeiten. Wir können verschiedene geeignete Kerne verwenden, die diese Merkmale erfassen.

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

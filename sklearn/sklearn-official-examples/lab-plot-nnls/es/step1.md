# Generar datos aleatorios

Generaremos algunos datos aleatorios para probar nuestro algoritmo. Crearemos 200 muestras con 50 características y usaremos un coeficiente real de 3 para cada característica. Luego, umbralizaremos los coeficientes para que sean no negativos. Por último, agregaremos algo de ruido a las muestras.

```python
import numpy as np

np.random.seed(42)

n_samples, n_features = 200, 50
X = np.random.randn(n_samples, n_features)
true_coef = 3 * np.random.randn(n_features)
true_coef[true_coef < 0] = 0
y = np.dot(X, true_coef)
y += 5 * np.random.normal(size=(n_samples,))
```

# Graficar la log-verosimilitud marginal

Graficamos la log-verosimilitud marginal de ambos modelos.

```python
import numpy as np

ard_scores = -np.array(ard.scores_)
brr_scores = -np.array(brr.scores_)
plt.plot(ard_scores, color="navy", label="ARD")
plt.plot(brr_scores, color="red", label="BayesianRidge")
plt.ylabel("Log-verosimilitud")
plt.xlabel("Iteraciones")
plt.xlim(1, 30)
plt.legend()
_ = plt.title("Log-verosimilitud de los modelos")
```

# Plotar a Log-verossimilhança Marginal

Plotamos a log-verossimilhança marginal de ambos os modelos.

```python
import numpy as np

ard_scores = -np.array(ard.scores_)
brr_scores = -np.array(brr.scores_)
plt.plot(ard_scores, color="navy", label="ARD")
plt.plot(brr_scores, color="red", label="BayesianRidge")
plt.ylabel("Log-verossimilhança")
plt.xlabel("Iterações")
plt.xlim(1, 30)
plt.legend()
_ = plt.title("Log-verossimilhança dos Modelos")
```

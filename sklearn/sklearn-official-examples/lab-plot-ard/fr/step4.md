# Tracer la log-vraisemblance marginale

Nous traçons la log-vraisemblance marginale des deux modèles.

```python
import numpy as np

ard_scores = -np.array(ard.scores_)
brr_scores = -np.array(brr.scores_)
plt.plot(ard_scores, color="navy", label="ARD")
plt.plot(brr_scores, color="red", label="BayesianRidge")
plt.ylabel("Log-vraisemblance")
plt.xlabel("Itérations")
plt.xlim(1, 30)
plt.legend()
_ = plt.title("Log-vraisemblance des modèles")
```

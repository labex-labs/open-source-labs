# Die marginale Log-Wahrscheinlichkeit plotten

Wir plotten die marginale Log-Wahrscheinlichkeit beider Modelle.

```python
import numpy as np

ard_scores = -np.array(ard.scores_)
brr_scores = -np.array(brr.scores_)
plt.plot(ard_scores, color="navy", label="ARD")
plt.plot(brr_scores, color="red", label="BayesianRidge")
plt.ylabel("Log-Wahrscheinlichkeit")
plt.xlabel("Iterationen")
plt.xlim(1, 30)
plt.legend()
_ = plt.title("Log-Wahrscheinlichkeit der Modelle")
```

# Построение графика предельной лог-вероятности

Мы строим график предельной лог-вероятности для обеих моделей.

```python
import numpy as np

ard_scores = -np.array(ard.scores_)
brr_scores = -np.array(brr.scores_)
plt.plot(ard_scores, color="navy", label="ARD")
plt.plot(brr_scores, color="red", label="BayesianRidge")
plt.ylabel("Log-вероятность")
plt.xlabel("Итерации")
plt.xlim(1, 30)
plt.legend()
_ = plt.title("Лог-вероятность моделей")
```

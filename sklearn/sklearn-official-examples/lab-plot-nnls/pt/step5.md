# Comparar Coeficientes de Regressão

Agora, compararemos os coeficientes de regressão entre a regressão de mínimos quadrados não negativos e a regressão linear clássica. Vamos plotar os coeficientes um contra o outro e observar que eles estão altamente correlacionados. No entanto, a restrição não negativa reduz alguns coeficientes a 0. Isto porque a regressão de mínimos quadrados não negativos inerentemente produz resultados esparsos.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(reg_ols.coef_, reg_nnls.coef_, linewidth=0, marker=".")

low_x, high_x = ax.get_xlim()
low_y, high_y = ax.get_ylim()
low = max(low_x, low_y)
high = min(high_x, high_y)
ax.plot([low, high], [low, high], ls="--", c=".3", alpha=0.5)
ax.set_xlabel("Coeficientes de regressão OLS", fontweight="bold")
ax.set_ylabel("Coeficientes de regressão NNLS", fontweight="bold")
```

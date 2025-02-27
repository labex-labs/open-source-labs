# Comparar los coeficientes de regresión

Ahora compararemos los coeficientes de regresión entre la regresión de mínimos cuadrados no negativos y la regresión lineal clásica. Graficaremos los coeficientes uno contra el otro y observaremos que están altamente correlacionados. Sin embargo, la restricción no negativa reduce algunos coeficientes a 0. Esto se debe a que la regresión de mínimos cuadrados no negativos inherentemente produce resultados dispersos.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(reg_ols.coef_, reg_nnls.coef_, linewidth=0, marker=".")

low_x, high_x = ax.get_xlim()
low_y, high_y = ax.get_ylim()
low = max(low_x, low_y)
high = min(high_x, high_y)
ax.plot([low, high], [low, high], ls="--", c=".3", alpha=0.5)
ax.set_xlabel("OLS regression coefficients", fontweight="bold")
ax.set_ylabel("NNLS regression coefficients", fontweight="bold")
```

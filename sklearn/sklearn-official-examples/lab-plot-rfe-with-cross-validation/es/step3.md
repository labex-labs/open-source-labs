# Graficar el número de características vs. puntuaciones de validación cruzada

Graficaremos el número de características seleccionadas en función de las puntuaciones de validación cruzada. Usaremos matplotlib para crear la gráfica.

```python
import matplotlib.pyplot as plt

n_scores = len(rfecv.cv_results_["mean_test_score"])
plt.figure()
plt.xlabel("Número de características seleccionadas")
plt.ylabel("Exactitud promedio en la prueba")
plt.errorbar(
    range(min_features_to_select, n_scores + min_features_to_select),
    rfecv.cv_results_["mean_test_score"],
    yerr=rfecv.cv_results_["std_test_score"],
)
plt.title("Eliminación recursiva de características \ncon características correlacionadas")
plt.show()
```

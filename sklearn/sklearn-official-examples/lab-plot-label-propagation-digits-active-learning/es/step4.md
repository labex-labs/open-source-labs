# Seleccionar los puntos más inciertos

Seleccionaremos los cinco puntos más inciertos basados en sus distribuciones de etiquetas predichas y solicitaremos sus etiquetas manuales.

```python
from scipy import stats

pred_entropies = stats.distributions.entropy(lp_model.label_distributions_.T)
uncertainty_index = np.argsort(pred_entropies)[::-1]
uncertainty_index = uncertainty_index[np.in1d(uncertainty_index, unlabeled_indices)][:5]
```

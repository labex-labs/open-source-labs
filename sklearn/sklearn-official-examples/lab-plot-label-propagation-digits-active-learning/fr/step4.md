# Sélectionner les points les plus incertains

Nous allons sélectionner les cinq points les plus incertains en fonction de leurs distributions de prédiction d'étiquette et demander des étiquettes humaines pour eux.

```python
from scipy import stats

pred_entropies = stats.distributions.entropy(lp_model.label_distributions_.T)
uncertainty_index = np.argsort(pred_entropies)[::-1]
uncertainty_index = uncertainty_index[np.in1d(uncertainty_index, unlabeled_indices)][:5]
```

# Wähle die am ungewissesten Punkte

Wir werden die fünf am ungewissesten Punkte basierend auf ihren vorhergesagten Label-Verteilungen auswählen und für sie menschliche Labels anfordern.

```python
from scipy import stats

pred_entropies = stats.distributions.entropy(lp_model.label_distributions_.T)
uncertainty_index = np.argsort(pred_entropies)[::-1]
uncertainty_index = uncertainty_index[np.in1d(uncertainty_index, unlabeled_indices)][:5]
```

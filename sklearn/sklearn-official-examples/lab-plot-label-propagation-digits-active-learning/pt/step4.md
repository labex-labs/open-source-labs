# Selecionar os Pontos Mais Incertos

Selecionaremos os cinco pontos mais incertos com base nas suas distribuições de rótulos previstos e solicitaremos rótulos humanos para eles.

```python
from scipy import stats

pred_entropies = stats.distributions.entropy(lp_model.label_distributions_.T)
uncertainty_index = np.argsort(pred_entropies)[::-1]
uncertainty_index = uncertainty_index[np.in1d(uncertainty_index, unlabeled_indices)][:5]
```

# Выбор наиболее неопределенных точек

Мы выберем пять наиболее неопределенных точек на основе их распределений предсказанных меток и попросим ввести для них метки вручную.

```python
from scipy import stats

pred_entropies = stats.distributions.entropy(lp_model.label_distributions_.T)
uncertainty_index = np.argsort(pred_entropies)[::-1]
uncertainty_index = uncertainty_index[np.in1d(uncertainty_index, unlabeled_indices)][:5]
```

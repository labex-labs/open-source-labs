# 最も不確定なポイントを選択する

予測されたラベル分布に基づいて、最も不確定な上位 5 つのポイントを選択し、それらに対する人間によるラベルを要求します。

```python
from scipy import stats

pred_entropies = stats.distributions.entropy(lp_model.label_distributions_.T)
uncertainty_index = np.argsort(pred_entropies)[::-1]
uncertainty_index = uncertainty_index[np.in1d(uncertainty_index, unlabeled_indices)][:5]
```

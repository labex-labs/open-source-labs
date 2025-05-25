# 가장 불확실한 포인트 선택

예측된 레이블 분포를 기반으로 가장 불확실한 상위 5 개 포인트를 선택하고, 사용자에게 이에 대한 레이블을 요청합니다.

```python
from scipy import stats

pred_entropies = stats.distributions.entropy(lp_model.label_distributions_.T)
uncertainty_index = np.argsort(pred_entropies)[::-1]
uncertainty_index = uncertainty_index[np.in1d(uncertainty_index, unlabeled_indices)][:5]
```

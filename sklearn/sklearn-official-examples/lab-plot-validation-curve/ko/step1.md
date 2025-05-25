# 데이터셋 로딩

scikit-learn 에서 숫자 데이터셋을 로드하고 숫자 1 과 2 의 이진 분류를 위해 데이터의 일부를 선택하는 것으로 시작합니다.

```python
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
subset_mask = np.isin(y, [1, 2])  # 이진 분류: 1 대 2
X, y = X[subset_mask], y[subset_mask]
```

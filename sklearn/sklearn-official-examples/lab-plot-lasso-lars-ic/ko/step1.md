# 데이터 로드

scikit-learn 의 `load_diabetes` 메서드를 사용하여 당뇨병 데이터셋을 로드합니다.

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True, as_frame=True)
```

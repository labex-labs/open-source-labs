# 데이터셋 로드

이 단계에서는 scikit-learn 라이브러리에서 당뇨병 데이터셋을 로드하고 데이터를 표준화합니다.

```python
from sklearn import datasets

# 당뇨병 데이터셋 로드
X, y = datasets.load_diabetes(return_X_y=True)

# 데이터 표준화
X /= X.std(axis=0)
```

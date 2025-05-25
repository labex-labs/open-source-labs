# 데이터 로드

첫 번째 단계는 Scikit-Learn 에서 다이어베티스 데이터셋을 로드하는 것입니다.

```python
from sklearn import datasets

X, y = datasets.load_diabetes(return_X_y=True)
```

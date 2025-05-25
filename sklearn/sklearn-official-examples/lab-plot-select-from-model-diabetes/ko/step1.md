# 데이터 로드

scikit-learn 에서 당뇨병 데이터 세트를 로드하고 설명을 출력합니다.

```python
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target
print(diabetes.DESCR)
```

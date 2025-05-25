# 데이터 로드

scikit-learn 의 유방암 데이터셋을 사용할 것입니다. 이 데이터셋은 30 개의 특징과 환자가 악성 또는 양성 암을 가지고 있는지 여부를 나타내는 이진 목표 변수를 포함합니다.

```python
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
```

# 데이터 로드

먼저, 예측 모델을 학습하는 데 사용할 수 있는 데이터 세트를 로드해야 합니다. scikit-learn 의 당뇨병 데이터 세트를 사용할 것입니다. 이 데이터 세트는 당뇨병 환자에 대한 정보를 포함합니다.

```python
from sklearn.datasets import load_diabetes

# 당뇨병 데이터 세트 로드
diabetes = load_diabetes()

# 데이터를 학습 및 검증 세트로 분할
X_train, X_val, y_train, y_val = train_test_split(diabetes.data, diabetes.target, random_state=0)
```

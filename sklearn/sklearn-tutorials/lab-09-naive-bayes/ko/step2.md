# 데이터셋을 학습 및 테스트 세트로 분할

다음으로 `sklearn.model_selection` 모듈의 `train_test_split` 함수를 사용하여 데이터셋을 학습 및 테스트 세트로 분할합니다. 학습 세트는 나이브 베이즈 분류기를 학습하는 데 사용되고, 테스트 세트는 분류기의 성능을 평가하는 데 사용됩니다.

```python
from sklearn.model_selection import train_test_split

# 데이터셋을 학습 및 테스트 세트로 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

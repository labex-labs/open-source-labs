# 머신러닝을 위한 데이터셋 준비

머신러닝 모델을 데이터셋에 학습시키기 전에 데이터를 학습용과 테스트용으로 분할하여 준비해야 합니다. 이 작업은 scikit-learn 의 `train_test_split` 함수를 사용하여 수행할 수 있습니다.

```python
from sklearn.model_selection import train_test_split

# 데이터셋을 학습용과 테스트용으로 분할
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)
```

# 데이터셋 분할

다음으로, 데이터셋을 학습용 및 테스트용 데이터셋으로 분할합니다. 학습에는 데이터의 80%, 테스트에는 20% 를 사용할 것입니다.

```python
# 데이터를 학습/테스트 세트로 분할
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# 대상 변수를 학습/테스트 세트로 분할
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
```

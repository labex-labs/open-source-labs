# 학습 및 테스트 데이터 분할

scikit-learn 의 `train_test_split` 함수를 사용하여 데이터를 400 개의 학습 데이터셋과 200 개의 테스트 데이터셋으로 분할합니다.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=400, test_size=200, random_state=4)
```

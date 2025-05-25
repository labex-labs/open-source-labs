# 데이터 분할

scikit-learn 의 `train_test_split` 함수를 사용하여 데이터를 학습용과 테스트용으로 분할합니다.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

# 변환된 데이터로 나이브 베이즈 분류기를 학습합니다.

이 단계에서는 변환된 데이터로 나이브 베이즈 분류기를 학습합니다.

```python
nb = BernoulliNB()
nb.fit(X_transformed, y)
```

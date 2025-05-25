# 모델 평가

이제 검증 세트를 사용하여 학습된 모델을 평가하겠습니다. 여기서 사용된 평가 지표는 R-제곱 점수입니다.

```python
# 검증 세트에서 모델 평가
score = model.score(X_val, y_val)
print("검증 점수:", score)
```

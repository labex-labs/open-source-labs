# 로그 손실 비교

1,000 개의 테스트 샘플 예측에 대한 보정되지 않은 분류기와 보정된 분류기의 로그 손실을 비교합니다.

```python
from sklearn.metrics import log_loss

score = log_loss(y_test, clf_probs)
cal_score = log_loss(y_test, cal_clf_probs)

print("로그 손실:")
print(f" * 보정되지 않은 분류기: {score:.3f}")
print(f" * 보정된 분류기: {cal_score:.3f}")
```

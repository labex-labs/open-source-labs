# 파이프라인 평가

이 단계에서는 모델 점수를 계산하여 파이프라인의 성능을 평가합니다.

```python
print("model score: %.3f" % clf.score(X_test, y_test))
```

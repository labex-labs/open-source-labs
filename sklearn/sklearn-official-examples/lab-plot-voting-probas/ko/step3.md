# 모든 분류기의 클래스 확률 예측

모든 분류기의 클래스 확률을 `predict_proba()` 함수를 사용하여 예측합니다.

```python
probas = [c.fit(X, y).predict_proba(X) for c in (clf1, clf2, clf3, eclf)]
```

# VotingClassifier 초기화

그런 다음 가중치 `[1, 1, 5]`를 가진 소프트 - 보팅 VotingClassifier 를 초기화합니다. 이는 평균화된 확률을 계산할 때 RandomForestClassifier 의 예측 확률이 다른 분류기의 가중치보다 5 배 더 중요하게 반영됨을 의미합니다.

```python
eclf = VotingClassifier(
    estimators=[("lr", clf1), ("rf", clf2), ("gnb", clf3)],
    voting="soft",
    weights=[1, 1, 5],
)
```

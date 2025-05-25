# 조기 종료 사용 여부에 따른 점수 비교

이제 두 모델의 점수를 비교합니다.

```python
score_gb.append(gb.score(X_test, y_test))
score_gbes.append(gbes.score(X_test, y_test))
```

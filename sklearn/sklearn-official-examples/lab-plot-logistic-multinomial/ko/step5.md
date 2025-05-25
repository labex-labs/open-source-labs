# One-vs-Rest 로지스틱 회귀 모델 학습

이제 3 단계와 동일한 매개변수를 사용하여, multi-class 옵션을 `"ovr"`로 설정한 One-vs-Rest 로지스틱 회귀 모델을 학습합니다. 그런 다음 모델의 학습 점수를 출력합니다.

```python
clf = LogisticRegression(
        solver="sag", max_iter=100, random_state=42, multi_class="ovr"
    ).fit(X, y)

print("training score : %.3f (%s)" % (clf.score(X, y), "ovr"))
```

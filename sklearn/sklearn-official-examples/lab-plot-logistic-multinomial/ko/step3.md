# 다항 로지스틱 회귀 모델 학습

이제 scikit-learn 의 `LogisticRegression` 함수를 사용하여 다항 로지스틱 회귀 모델을 학습합니다. solver 를 `"sag"`로, 최대 반복 횟수를 100 으로, random state 를 42 로, multi-class 옵션을 `"multinomial"`로 설정합니다. 그런 다음 모델의 학습 점수를 출력합니다.

```python
clf = LogisticRegression(
        solver="sag", max_iter=100, random_state=42, multi_class="multinomial"
    ).fit(X, y)

print("training score : %.3f (%s)" % (clf.score(X, y), "multinomial"))
```

# 최적의 Alpha 값 결정

의사 결정 트리 가지치기에 사용할 최적의 alpha 값을 결정합니다. 이를 위해 학습 및 테스트 데이터셋에 대한 정확도와 alpha 값의 관계를 그래프로 나타낼 수 있습니다.

```python
train_scores = [clf.score(X_train, y_train) for clf in clfs]
test_scores = [clf.score(X_test, y_test) for clf in clfs]

fig, ax = plt.subplots()
ax.set_xlabel("alpha")
ax.set_ylabel("정확도")
ax.set_title("학습 및 테스트 데이터셋의 alpha 에 따른 정확도")
ax.plot(ccp_alphas, train_scores, marker="o", label="학습", drawstyle="steps-post")
ax.plot(ccp_alphas, test_scores, marker="o", label="테스트", drawstyle="steps-post")
ax.legend()
plt.show()
```

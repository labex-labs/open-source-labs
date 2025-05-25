# 분류기 훈련 및 평가

각 분류기를 훈련 데이터의 1% 에서 95% 까지의 비율로 훈련시키고, 테스트 데이터에서 성능을 평가합니다. 테스트 오류율의 더 정확한 추정치를 얻기 위해 이 과정을 10 번 반복합니다.

```python
heldout = [0.01, 0.05, 0.25, 0.5, 0.75, 0.9, 0.95]
rounds = 10
xx = 1.0 - np.array(heldout)

for name, clf in classifiers:
    print("Training %s" % name)
    yy = []
    for i in heldout:
        yy_ = []
        for r in range(rounds):
            X_train_, X_test_, y_train_, y_test_ = train_test_split(X_train, y_train, test_size=i, random_state=r)
            clf.fit(X_train_, y_train_)
            y_pred = clf.predict(X_test_)
            yy_.append(1 - np.mean(y_pred == y_test_))
        yy.append(np.mean(yy_))
    plt.plot(xx, yy, label=name)

plt.legend(loc="upper right")
plt.xlabel("훈련 데이터 비율")
plt.ylabel("테스트 오류율")
plt.show()
```

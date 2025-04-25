# 分類器を学習して評価する

学習データの 1％から 95％までの異なる割合で各分類器を学習し、テストセットでの性能を評価します。このプロセスを 10 回繰り返して、テスト誤差率のより正確な推定値を得ます。

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
plt.xlabel("Proportion of training data")
plt.ylabel("Test error rate")
plt.show()
```

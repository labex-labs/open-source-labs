# 分類器を学習と評価する

生成したデータで各分類器の性能を確認するため、それぞれの分類器を学習と評価します。このプロセスを複数回繰り返して平均的な正解率を得ます。

```python
n_train = 20  # 学習用のサンプル数
n_test = 200  # 評価用のサンプル数
n_averages = 50  # 分類を繰り返す回数
n_features_max = 75  # 最大の特徴数
step = 4  # 計算の刻み幅

acc_clf1, acc_clf2, acc_clf3 = [], [], []
n_features_range = range(1, n_features_max + 1, step)

for n_features in n_features_range:
    score_clf1, score_clf2, score_clf3 = 0, 0, 0
    for _ in range(n_averages):
        X, y = generate_data(n_train, n_features)

        clf1.fit(X, y)
        clf2.fit(X, y)
        clf3.fit(X, y)

        X, y = generate_data(n_test, n_features)
        score_clf1 += clf1.score(X, y)
        score_clf2 += clf2.score(X, y)
        score_clf3 += clf3.score(X, y)

    acc_clf1.append(score_clf1 / n_averages)
    acc_clf2.append(score_clf2 / n_averages)
    acc_clf3.append(score_clf3 / n_averages)
```

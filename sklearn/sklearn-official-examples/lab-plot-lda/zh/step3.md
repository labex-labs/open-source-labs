# 训练和测试分类器

我们将训练和测试每个分类器，以观察它们在生成的数据上的表现。我们将多次重复此过程，以获得平均准确率得分。

```python
n_train = 20  # 训练样本数
n_test = 200  # 测试样本数
n_averages = 50  # 重复分类的次数
n_features_max = 75  # 最大特征数
step = 4  # 计算的步长

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

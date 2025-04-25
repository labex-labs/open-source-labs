# 创建数据集

我们将使用 scikit-learn 中的 make_classification、make_moons 和 make_circles 函数创建三个合成数据集。我们将使用 train_test_split 将每个数据集拆分为训练集和测试集。

```python
X, y = make_classification(
    n_features=2, n_redundant=0, n_informative=2, random_state=0, n_clusters_per_class=1
)
rng = np.random.RandomState(2)
X += 2 * rng.uniform(size=X.shape)
linearly_separable = (X, y)

datasets = [
    make_moons(noise=0.3, random_state=0),
    make_circles(noise=0.2, factor=0.5, random_state=1),
    linearly_separable,
]

figure = plt.figure(figsize=(17, 9))
i = 1
# 遍历数据集
for X, y in datasets:
    # 拆分为训练和测试部分
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.4, random_state=42
    )
```

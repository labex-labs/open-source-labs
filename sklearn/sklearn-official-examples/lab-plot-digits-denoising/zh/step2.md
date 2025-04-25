# 创建训练集和测试集

我们将数据集拆分为一个包含 1000 个样本的训练集和一个包含 100 个样本的测试集。我们向测试集中添加高斯噪声，并创建原始数据的两个副本：一个有噪声，一个无噪声。

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, random_state=0, train_size=1_000, test_size=100
)

rng = np.random.RandomState(0)
noise = rng.normal(scale=0.25, size=X_test.shape)
X_test_noisy = X_test + noise

noise = rng.normal(scale=0.25, size=X_train.shape)
X_train_noisy = X_train + noise
```

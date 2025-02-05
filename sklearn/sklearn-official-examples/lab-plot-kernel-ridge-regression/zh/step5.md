# 可视化训练和预测时间

我们将可视化不同训练集大小下核岭回归（KRR）和支持向量回归（SVR）的拟合时间和预测时间。

```python
_, ax = plt.subplots()

sizes = np.logspace(1, 3.8, 7).astype(int)
for name, estimator in {
    "KRR": KernelRidge(kernel="rbf", alpha=0.01, gamma=10),
    "SVR": SVR(kernel="rbf", C=1e2, gamma=10),
}.items():
    train_time = []
    test_time = []
    for train_test_size in sizes:
        t0 = time.time()
        estimator.fit(X[:train_test_size], y[:train_test_size])
        train_time.append(time.time() - t0)

        t0 = time.time()
        estimator.predict(X_plot[:1000])
        test_time.append(time.time() - t0)

    plt.plot(
        sizes,
        train_time,
        "o-",
        color="r" if name == "SVR" else "g",
        label="%s（训练）" % name,
    )
    plt.plot(
        sizes,
        test_time,
        "o--",
        color="r" if name == "SVR" else "g",
        label="%s（测试）" % name,
    )

plt.xscale("log")
plt.yscale("log")
plt.xlabel("训练集大小")
plt.ylabel("时间（秒）")
plt.title("执行时间")
_ = plt.legend(loc="best")
```

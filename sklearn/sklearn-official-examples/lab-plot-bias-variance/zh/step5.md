# 训练模型并计算预期均方误差

我们将遍历这些估计器，在多个训练集上对它们进行训练，并通过将均方误差分解为偏差、方差和噪声项来计算预期均方误差。我们还将绘制模型的预测结果以及偏差 - 方差分解图。

```python
plt.figure(figsize=(10, 8))

# 遍历估计器进行比较
for n, (name, estimator) in enumerate(estimators):
    # 计算预测值
    y_predict = np.zeros((n_test, n_repeat))

    for i in range(n_repeat):
        estimator.fit(X_train[i], y_train[i])
        y_predict[:, i] = estimator.predict(X_test)

    # 均方误差的偏差^2 + 方差 + 噪声分解
    y_error = np.zeros(n_test)

    for i in range(n_repeat):
        for j in range(n_repeat):
            y_error += (y_test[:, j] - y_predict[:, i]) ** 2

    y_error /= n_repeat * n_repeat

    y_noise = np.var(y_test, axis=1)
    y_bias = (f(X_test) - np.mean(y_predict, axis=1)) ** 2
    y_var = np.var(y_predict, axis=1)

    print(
        "{0}: {1:.4f} (误差) = {2:.4f} (偏差^2) "
        " + {3:.4f} (方差) + {4:.4f} (噪声)".format(
            name, np.mean(y_error), np.mean(y_bias), np.mean(y_var), np.mean(y_noise)
        )
    )

    # 绘制图形
    plt.subplot(2, n_estimators, n + 1)
    plt.plot(X_test, f(X_test), "b", label="$f(x)$")
    plt.plot(X_train[0], y_train[0], ".b", label="最小二乘 ~ $y = f(x)+噪声$")

    for i in range(n_repeat):
        if i == 0:
            plt.plot(X_test, y_predict[:, i], "r", label=r"$\^y(x)$")
        else:
            plt.plot(X_test, y_predict[:, i], "r", alpha=0.05)

    plt.plot(X_test, np.mean(y_predict, axis=1), "c", label=r"$\mathbb{E}_{LS} \^y(x)$")

    plt.xlim([-5, 5])
    plt.title(name)

    if n == n_estimators - 1:
        plt.legend(loc=(1.1, 0.5))

    plt.subplot(2, n_estimators, n_estimators + n + 1)
    plt.plot(X_test, y_error, "r", label="$误差(x)$")
    plt.plot(X_test, y_bias, "b", label="$偏差^2(x)$"),
    plt.plot(X_test, y_var, "g", label="$方差(x)$"),
    plt.plot(X_test, y_noise, "c", label="$噪声(x)$")

    plt.xlim([-5, 5])
    plt.ylim([0, 0.1])

    if n == n_estimators - 1:
        plt.legend(loc=(1.1, 0.5))

plt.subplots_adjust(right=0.75)
plt.show()
```

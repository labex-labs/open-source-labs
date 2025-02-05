# 绘制结果函数

我们将使用`matplotlib`库来绘制结果函数。我们将使用`plt.subplot()`函数创建两个子图。在第一个子图中，我们将绘制训练误差和测试误差作为正则化参数的函数。我们还将在最优正则化参数处绘制一条垂直线。在第二个子图中，我们将绘制真实系数和估计系数。

```python
import matplotlib.pyplot as plt

plt.subplot(2, 1, 1)
plt.semilogx(alphas, train_errors, label="Train")
plt.semilogx(alphas, test_errors, label="Test")
plt.vlines(
    alpha_optim,
    plt.ylim()[0],
    np.max(test_errors),
    color="k",
    linewidth=3,
    label="Optimum on test",
)
plt.legend(loc="lower right")
plt.ylim([0, 1.2])
plt.xlabel("Regularization parameter")
plt.ylabel("Performance")

# 显示估计的系数coef_与真实系数
plt.subplot(2, 1, 2)
plt.plot(coef, label="True coef")
plt.plot(coef_, label="Estimated coef")
plt.legend()
plt.subplots_adjust(0.09, 0.04, 0.94, 0.94, 0.26, 0.26)
plt.show()
```

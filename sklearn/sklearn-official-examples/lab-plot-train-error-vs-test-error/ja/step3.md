# 結果関数のプロット

`matplotlib`ライブラリを使って結果関数をプロットします。`plt.subplot()`関数を使って 2 つのサブプロットを作成します。最初のサブプロットでは、正則化パラメータの関数として学習誤差とテスト誤差をプロットします。また、最適な正則化パラメータのところに垂直線をプロットします。2 番目のサブプロットでは、真の係数と推定された係数をプロットします。

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

# Show estimated coef_ vs true coef
plt.subplot(2, 1, 2)
plt.plot(coef, label="True coef")
plt.plot(coef_, label="Estimated coef")
plt.legend()
plt.subplots_adjust(0.09, 0.04, 0.94, 0.94, 0.26, 0.26)
plt.show()
```

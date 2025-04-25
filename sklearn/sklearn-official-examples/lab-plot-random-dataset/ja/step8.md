# 3 つの四分位数に分割されたガウス分布

3 つの四分位数に分割されたガウス分布を持つデータセットを作成し、プロットします。

```python
plt.subplot(326)
plt.title("Gaussian divided into three quantiles", fontsize="small")
X1, Y1 = make_gaussian_quantiles(n_features=2, n_classes=3)
plt.scatter(X1[:, 0], X1[:, 1], marker="o", c=Y1, s=25, edgecolor="k")
```

# 線形スケールでプロットを作成する

線形スケールでプロットを作成します。これは、`plot()` を使用して正規分布、ラプラス分布、コーシー分布の累積分布関数を単にプロットし、`legend()` を使用して凡例を追加することで行えます。

```python
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(6.4, 4.8))

axs.plot(x, cdf_norm, label=r"$\mathcal{N}$")
axs.plot(x, cdf_laplacian, label=r"$\mathcal{L}$")
axs.plot(x, cdf_cauchy, label="Cauchy")
axs.legend()
axs.grid()

plt.show()
```

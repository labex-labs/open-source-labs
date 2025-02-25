# 対数オッド比スケールと標準表記でプロットを作成する

対数オッド比スケールと標準表記でプロットを作成します。これは、`set_yscale("logit")` を使用して y 軸のスケールを対数オッド比に設定し、`set_ylim()` を使用して y 軸の範囲を設定することで行えます。また、`plot()` を使用して正規分布、ラプラス分布、コーシー分布の累積分布関数をプロットし、`legend()` を使用して凡例を追加します。

```python
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(6.4, 4.8))

axs.plot(x, cdf_norm, label=r"$\mathcal{N}$")
axs.plot(x, cdf_laplacian, label=r"$\mathcal{L}$")
axs.plot(x, cdf_cauchy, label="Cauchy")
axs.set_yscale("logit")
axs.set_ylim(1e-5, 1 - 1e-5)
axs.legend()
axs.grid()

plt.show()
```

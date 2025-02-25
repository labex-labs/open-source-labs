# 対数オッド比スケールと生存表記でプロットを作成する

対数オッド比スケールと生存表記でプロットを作成します。これは、y軸のスケールを対数オッド比に設定し、`set_yscale("logit", one_half="1/2", use_overline=True)"` を使用して `one_half` パラメータを `"1/2"` に、`use_overline` パラメータを `True` に設定することで行えます。また、`plot()` を使用して正規分布、ラプラス分布、コーシー分布の累積分布関数をプロットし、`legend()` を使用して凡例を追加します。

```python
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(6.4, 4.8))

axs.plot(x, cdf_norm, label=r"$\mathcal{N}$")
axs.plot(x, cdf_laplacian, label=r"$\mathcal{L}$")
axs.plot(x, cdf_cauchy, label="Cauchy")
axs.set_yscale("logit", one_half="1/2", use_overline=True)
axs.set_ylim(1e-5, 1 - 1e-5)
axs.legend()
axs.grid()

plt.show()
```

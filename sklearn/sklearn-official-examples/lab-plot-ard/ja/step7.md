# スコアの標準誤差付きの多項式回帰のプロット

誤差バーは、照会ポイントの予測ガウス分布の1標準偏差を表します。両モデルのデフォルトパラメータを使用した場合、ARD回帰が真の値を最も良く捉えていることに注意してください。ただし、ベイジアンリッジの`lambda_init`ハイパーパラメータをさらに減らすことで、そのバイアスを低減できます。最後に、多項式回帰の固有の制限のため、両モデルは外挿時に失敗します。

```python
ax = sns.scatterplot(
    data=full_data, x="input_feature", y="target", color="black", alpha=0.75
)
ax.plot(X_plot, y_plot, color="black", label="Ground Truth")
ax.plot(X_plot, y_brr, color="red", label="BayesianRidge with polynomial features")
ax.plot(X_plot, y_ard, color="navy", label="ARD with polynomial features")
ax.fill_between(
    X_plot.ravel(),
    y_ard - y_ard_std,
    y_ard + y_ard_std,
    color="navy",
    alpha=0.3,
)
ax.fill_between(
    X_plot.ravel(),
    y_brr - y_brr_std,
    y_brr + y_brr_std,
    color="red",
    alpha=0.3,
)
ax.legend()
_ = ax.set_title("Polynomial fit of a non-linear feature")
```

# 1 次元密度の例の描画

1 次元で 100 個のサンプルを持つ 1 次元密度の例を描画します。トップハット、ガウス、エパネチニコフの 3 種類の異なるカーネル密度推定を比較します。

```python
# データを生成
N = 100
np.random.seed(1)
X = np.concatenate(
    (np.random.normal(0, 1, int(0.3 * N)), np.random.normal(5, 1, int(0.7 * N)))
)[:, np.newaxis]

X_plot = np.linspace(-5, 10, 1000)[:, np.newaxis]

true_dens = 0.3 * norm(0, 1).pdf(X_plot[:, 0]) + 0.7 * norm(5, 1).pdf(X_plot[:, 0])

# グラフと軸を作成
fig, ax = plt.subplots()

# 入力分布を描画
ax.fill(X_plot[:, 0], true_dens, fc="black", alpha=0.2, label="入力分布")

# 色とカーネルを設定
colors = ["navy", "cornflowerblue", "darkorange"]
kernels = ["gaussian", "tophat", "epanechnikov"]
lw = 2

# カーネル密度推定を描画
for color, kernel in zip(colors, kernels):
    kde = KernelDensity(kernel=kernel, bandwidth=0.5).fit(X)
    log_dens = kde.score_samples(X_plot)
    ax.plot(
        X_plot[:, 0],
        np.exp(log_dens),
        color=color,
        lw=lw,
        linestyle="-",
        label="kernel = '{0}'".format(kernel),
    )

ax.text(6, 0.38, "N={0} points".format(N))

# 凡例を設定してデータポイントを描画
ax.legend(loc="upper left")
ax.plot(X[:, 0], -0.005 - 0.01 * np.random.random(X.shape[0]), "+k")

# x と y の範囲を設定
ax.set_xlim(-4, 9)
ax.set_ylim(-0.02, 0.4)

# グラフを表示
plt.show()
```

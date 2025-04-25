# 绘制一维密度示例

我们将绘制一个一维密度示例，其中包含 100 个样本。我们将比较三种不同的核密度估计：顶帽核（tophat）、高斯核（Gaussian）和叶甫根尼科夫核（epanechnikov）。

```python
# 生成数据
N = 100
np.random.seed(1)
X = np.concatenate(
    (np.random.normal(0, 1, int(0.3 * N)), np.random.normal(5, 1, int(0.7 * N)))
)[:, np.newaxis]

X_plot = np.linspace(-5, 10, 1000)[:, np.newaxis]

true_dens = 0.3 * norm(0, 1).pdf(X_plot[:, 0]) + 0.7 * norm(5, 1).pdf(X_plot[:, 0])

# 创建图形和坐标轴
fig, ax = plt.subplots()

# 绘制输入分布
ax.fill(X_plot[:, 0], true_dens, fc="black", alpha=0.2, label="输入分布")

# 设置颜色和核函数
colors = ["海军蓝", "矢车菊蓝", "深橙色"]
kernels = ["高斯核", "顶帽核", "叶甫根尼科夫核"]
lw = 2

# 绘制核密度估计
for color, kernel in zip(colors, kernels):
    kde = KernelDensity(kernel=kernel, bandwidth=0.5).fit(X)
    log_dens = kde.score_samples(X_plot)
    ax.plot(
        X_plot[:, 0],
        np.exp(log_dens),
        color=color,
        lw=lw,
        linestyle="-",
        label="核函数 = '{0}'".format(kernel),
    )

ax.text(6, 0.38, "N={0} 个点".format(N))

# 设置图例并绘制数据点
ax.legend(loc="左上角")
ax.plot(X[:, 0], -0.005 - 0.01 * np.random.random(X.shape[0]), "+k")

# 设置 x 和 y 轴范围
ax.set_xlim(-4, 9)
ax.set_ylim(-0.02, 0.4)

# 显示图形
plt.show()
```

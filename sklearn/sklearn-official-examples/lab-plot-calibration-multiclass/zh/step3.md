# 比较概率

我们绘制一个二维单纯形，并使用箭头展示测试样本预测概率的变化。

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 10))
colors = ["r", "g", "b"]

clf_probs = clf.predict_proba(X_test)
cal_clf_probs = cal_clf.predict_proba(X_test)
# 绘制箭头
for i in range(clf_probs.shape[0]):
    plt.arrow(
        clf_probs[i, 0],
        clf_probs[i, 1],
        cal_clf_probs[i, 0] - clf_probs[i, 0],
        cal_clf_probs[i, 1] - clf_probs[i, 1],
        color=colors[y_test[i]],
        head_width=1e-2,
    )

# 在每个顶点绘制完美预测
plt.plot([1.0], [0.0], "ro", ms=20, label="类别1")
plt.plot([0.0], [1.0], "go", ms=20, label="类别2")
plt.plot([0.0], [0.0], "bo", ms=20, label="类别3")

# 绘制单位单纯形的边界
plt.plot([0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], "k", label="单纯形")

# 在单纯形周围注释6个点，并在单纯形内部注释中点
plt.annotate(
    r"($\frac{1}{3}$, $\frac{1}{3}$, $\frac{1}{3}$)",
    xy=(1.0 / 3, 1.0 / 3),
    xytext=(1.0 / 3, 0.23),
    xycoords="数据",
    arrowprops=dict(facecolor="黑色", shrink=0.05),
    horizontalalignment="中心",
    verticalalignment="中心",
)
plt.plot([1.0 / 3], [1.0 / 3], "ko", ms=5)
plt.annotate(
    r"($\frac{1}{2}$, $0$, $\frac{1}{2}$)",
    xy=(0.5, 0.0),
    xytext=(0.5, 0.1),
    xycoords="数据",
    arrowprops=dict(facecolor="黑色", shrink=0.05),
    horizontalalignment="中心",
    verticalalignment="中心",
)
plt.annotate(
    r"($0$, $\frac{1}{2}$, $\frac{1}{2}$)",
    xy=(0.0, 0.5),
    xytext=(0.1, 0.5),
    xycoords="数据",
    arrowprops=dict(facecolor="黑色", shrink=0.05),
    horizontalalignment="中心",
    verticalalignment="中心",
)
plt.annotate(
    r"($\frac{1}{2}$, $\frac{1}{2}$, $0$)",
    xy=(0.5, 0.5),
    xytext=(0.6, 0.6),
    xycoords="数据",
    arrowprops=dict(facecolor="黑色", shrink=0.05),
    horizontalalignment="中心",
    verticalalignment="中心",
)
plt.annotate(
    r"($0$, $0$, $1$)",
    xy=(0, 0),
    xytext=(0.1, 0.1),
    xycoords="数据",
    arrowprops=dict(facecolor="黑色", shrink=0.05),
    horizontalalignment="中心",
    verticalalignment="中心",
)
plt.annotate(
    r"($1$, $0$, $0$)",
    xy=(1, 0),
    xytext=(1, 0.1),
    xycoords="数据",
    arrowprops=dict(facecolor="黑色", shrink=0.05),
    horizontalalignment="中心",
    verticalalignment="中心",
)
plt.annotate(
    r"($0$, $1$, $0$)",
    xy=(0, 1),
    xytext=(0.1, 1),
    xycoords="数据",
    arrowprops=dict(facecolor="黑色", shrink=0.05),
    horizontalalignment="中心",
    verticalalignment="中心",
)
# 添加网格
plt.grid(False)
for x in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
    plt.plot([0, x], [x, 0], "k", alpha=0.2)
    plt.plot([0, 0 + (1 - x) / 2], [x, x + (1 - x) / 2], "k", alpha=0.2)
    plt.plot([x, x + (1 - x) / 2], [0, 0 + (1 - x) / 2], "k", alpha=0.2)

plt.title("sigmoid校准后测试样本预测概率的变化")
plt.xlabel("类别1的概率")
plt.ylabel("类别2的概率")
plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.05)
_ = plt.legend(loc="最佳")
```

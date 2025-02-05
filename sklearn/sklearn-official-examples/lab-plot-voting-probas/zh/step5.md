# 绘制类别概率

我们将使用柱状图绘制每个分类器和投票分类器的类别概率。

```python
N = 4  # 组数
ind = np.arange(N)  # 组位置
width = 0.35  # 柱状图宽度

fig, ax = plt.subplots()

# 分类器1 - 3的柱状图
p1 = ax.bar(ind, np.hstack(([class1_1[:-1], [0]])), width, color="green", edgecolor="k")
p2 = ax.bar(
    ind + width,
    np.hstack(([class2_1[:-1], [0]])),
    width,
    color="lightgreen",
    edgecolor="k",
)

# 投票分类器的柱状图
p3 = ax.bar(ind, [0, 0, 0, class1_1[-1]], width, color="blue", edgecolor="k")
p4 = ax.bar(
    ind + width, [0, 0, 0, class2_1[-1]], width, color="steelblue", edgecolor="k"
)

# 绘制注释
plt.axvline(2.8, color="k", linestyle="dashed")
ax.set_xticks(ind + width)
ax.set_xticklabels(
    [
        "逻辑回归\n权重1",
        "高斯朴素贝叶斯\n权重1",
        "随机森林分类器\n权重5",
        "投票分类器\n（平均概率）",
    ],
    rotation=40,
    ha="right",
)
plt.ylim([0, 1])
plt.title("不同分类器对样本1的类别概率")
plt.legend([p1[0], p2[0]], ["类别1", "类别2"], loc="upper left")
plt.tight_layout()
plt.show()
```

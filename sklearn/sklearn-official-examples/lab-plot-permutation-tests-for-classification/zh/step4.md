# 绘制结果

我们绘制了原始鸢尾花数据集和随机化数据的排列分数（零分布）的直方图。我们还用红线表示分类器在原始数据上获得的分数。每个图上都显示了 p 值。

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# 原始数据
ax.hist(perm_scores_iris, bins=20, density=True)
ax.axvline(score_iris, ls="--", color="r")
score_label = f"Score on original\ndata: {score_iris:.2f}\n(p-value: {pvalue_iris:.3f})"
ax.text(0.7, 10, score_label, fontsize=12)
ax.set_xlabel("Accuracy score")
_ = ax.set_ylabel("Probability density")

plt.show()

fig, ax = plt.subplots()

# 随机数据
ax.hist(perm_scores_rand, bins=20, density=True)
ax.set_xlim(0.13)
ax.axvline(score_rand, ls="--", color="r")
score_label = f"Score on original\ndata: {score_rand:.2f}\n(p-value: {pvalue_rand:.3f})"
ax.text(0.14, 7.5, score_label, fontsize=12)
ax.set_xlabel("Accuracy score")
ax.set_ylabel("Probability density")

plt.show()
```

# 绘制分类准确率

我们将绘制每个成分数量下的分类准确率。

```python
best_clfs.plot(
    x=components_col, y="mean_test_score", yerr="std_test_score", legend=False, ax=ax1
)
ax1.set_ylabel("分类准确率(验证集)")
ax1.set_xlabel("成分数量")

plt.xlim(-1, 70)

plt.tight_layout()
plt.show()
```

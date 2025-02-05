# 可视化结果

在这一步中，我们将可视化特征离散化过程的结果。我们将绘制每个分类器和数据集在测试集上的分类准确率。

```python
plt.tight_layout()

# 在图形上方添加总标题
plt.subplots_adjust(top=0.90)
总标题 = [
    "线性分类器",
    "特征离散化与线性分类器",
    "非线性分类器",
]
for i, 总标题 in zip([1, 3, 5], 总标题):
    ax = axes[0, i]
    ax.text(
        1.05,
        1.25,
        总标题,
        transform=ax.transAxes,
        horizontalalignment="center",
        size="x-large",
    )
plt.show()
```

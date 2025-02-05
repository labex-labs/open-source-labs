# 绘制比较特征选择的图表

我们可以绘制每个特征的特征得分和权重，以查看单变量特征选择的影响。

```python
plt.bar(
    X_indices - 0.45, scores, width=0.2, label=r"单变量得分（$-Log(p_{值})$）"
)

plt.bar(X_indices - 0.25, svm_weights, width=0.2, label="支持向量机权重")

plt.bar(
    X_indices[selector.get_support()] - 0.05,
    svm_weights_selected,
    width=0.2,
    label="选择后的支持向量机权重",
)

plt.title("比较特征选择")
plt.xlabel("特征编号")
plt.yticks(())
plt.axis("tight")
plt.legend(loc="upper right")
plt.show()
```

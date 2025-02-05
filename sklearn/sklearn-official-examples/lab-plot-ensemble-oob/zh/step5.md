# 可视化袋外（OOB）错误率

最后，我们将绘制每个分类器的 OOB 错误率与估计器数量的函数关系图。这将使我们能够确定错误率趋于稳定时的估计器数量。我们将使用 Matplotlib 来生成该图。

```python
for label, clf_err in error_rate.items():
    xs, ys = zip(*clf_err)
    plt.plot(xs, ys, label=label)

plt.xlim(min_estimators, max_estimators)
plt.xlabel("n_estimators")
plt.ylabel("OOB error rate")
plt.legend(loc="upper right")
plt.show()
```

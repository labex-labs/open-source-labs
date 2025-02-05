# 预测未知实例的聚类成员身份

在这一步中，我们将使用归纳学习模型来预测生成的新样本的聚类成员身份。我们将使用 `InductiveClusterer` 类的 `predict` 函数，并绘制新样本及其可能所属的聚类。

```python
probable_clusters = inductive_learner.predict(X_new)

plt.subplot(133)
plot_scatter(X, cluster_labels)
plot_scatter(X_new, probable_clusters)
plt.title("Classify unknown instances")
```

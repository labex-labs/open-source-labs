# 去除元数据后的模型

现在我们将使用scikit-learn中20新闻组数据集加载器的`remove`选项来训练一个文本分类器，该分类器在做决策时不太依赖元数据。我们还将使用混淆矩阵分析测试集上的分类错误，并检查定义训练模型分类函数的系数。

```python
(
    X_train,
    X_test,
    y_train,
    y_test,
    feature_names,
    target_names,
) = load_dataset(remove=("headers", "footers", "quotes"))

clf = RidgeClassifier(tol=1e-2, solver="sparse_cg")
clf.fit(X_train, y_train)
pred = clf.predict(X_test)

fig, ax = plt.subplots(figsize=(10, 5))
ConfusionMatrixDisplay.from_predictions(y_test, pred, ax=ax)
ax.xaxis.set_ticklabels(target_names)
ax.yaxis.set_ticklabels(target_names)
_ = ax.set_title(
    f"{clf.__class__.__name__} 的混淆矩阵\n在过滤后的文档上"
)

_ = plot_feature_effects().set_title("对过滤后文档的平均特征效应")
```

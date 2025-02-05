# 从混淆矩阵重建分类报告

如果评估分类器的结果以混淆矩阵的形式存储，而不是以`y_true`和`y_pred`的形式存储，我们仍然可以使用`metrics.classification_report()`方法按如下方式构建分类报告：

```python
y_true = []
y_pred = []
cm = disp.confusion_matrix

for gt in range(len(cm)):
    for pred in range(len(cm)):
        y_true += [gt] * cm[gt][pred]
        y_pred += [pred] * cm[gt][pred]

print(
    "Classification report rebuilt from confusion matrix:\n"
    f"{metrics.classification_report(y_true, y_pred)}\n"
)
```

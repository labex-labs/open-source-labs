# 评估模型

现在我们将使用验证集来评估训练好的模型。这里使用的评估指标是决定系数（R-squared score）。

```python
# 在验证集上评估模型
score = model.score(X_val, y_val)
print("验证分数:", score)
```

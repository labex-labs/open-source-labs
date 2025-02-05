# 拟合模型并进行预测

我们将拟合模型并在评估集上进行预测。

```python
grid_search.fit(X_train, y_train)

# 网格搜索使用我们的自定义策略选择的参数是：
grid_search.best_params_

# 最后，我们在留出的评估集上评估微调后的模型：`grid_search` 对象 **已使用我们的自定义重新拟合策略选择的参数在完整训练集上自动重新拟合**。
y_pred = grid_search.predict(X_test)
print(classification_report(y_test, y_pred))
```

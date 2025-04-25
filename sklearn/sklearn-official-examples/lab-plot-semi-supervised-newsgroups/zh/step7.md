# 训练和评估标签传播模型

在这一步中，我们将对 20% 的已标注数据使用标签传播方法。我们将随机选择 20% 的已标注数据，在这些数据上训练模型，然后使用该模型为其余未标注数据预测标签。

```python
# 训练并评估标签传播管道
ls_pipeline.fit(X_train, y_train)
y_pred = ls_pipeline.predict(X_test)
print(
    "测试集上的微平均 F1 分数：%0.3f"
    % f1_score(y_test, y_pred, average="micro")
)
```

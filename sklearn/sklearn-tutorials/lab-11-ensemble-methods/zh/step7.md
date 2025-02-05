# 评估随机森林分类器

让我们通过计算测试数据上的准确率得分来评估随机森林分类器。

```python
accuracy = random_forest.score(X_test, y_test)
print(f"Random Forest Classifier Accuracy: {accuracy}")
```

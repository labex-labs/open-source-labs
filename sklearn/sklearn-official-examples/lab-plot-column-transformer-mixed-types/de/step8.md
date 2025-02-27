#计算管道的性能

在这一步中，我们将通过计算模型得分来评估管道的性能。

```python
print("model score: %.3f" % clf.score(X_test, y_test))
```

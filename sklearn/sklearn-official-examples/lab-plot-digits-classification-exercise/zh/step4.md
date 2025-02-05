# 训练和测试K近邻分类器

现在我们将使用scikit-learn的`KNeighborsClassifier`函数训练一个K近邻（KNN）分类器，并在测试集上进行测试。然后我们将打印分类器的准确率得分。

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
knn_score = knn.score(X_test, y_test)

print("KNN score: %f" % knn_score)
```

# 训练机器学习模型

既然我们已经准备好数据集，就可以在训练数据上训练机器学习模型了。在这个例子中，我们将使用支持向量机（SVM）算法：

```python
from sklearn.svm import SVC

# 创建 SVM 分类器
clf = SVC(kernel='linear')

# 使用训练数据训练分类器
clf.fit(X_train, y_train)
```

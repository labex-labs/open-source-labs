# 管道 - 链接估计器

scikit-learn 中的 `Pipeline` 类用于将多个估计器链接成一个。这使你能够对数据调用一次 `fit` 和 `predict`，以拟合一整个估计器序列。它还允许进行联合参数选择，并有助于避免在交叉验证中出现数据泄露。

要创建一个管道，你需要提供一个 `(键, 值)` 对的列表，其中 `键` 是用于标识每个步骤的字符串，`值` 是一个估计器对象。以下是创建一个包含 PCA 转换器和 SVM 分类器的管道的示例：

```python
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA

estimators = [('reduce_dim', PCA()), ('clf', SVC())]
pipe = Pipeline(estimators)
```

你可以使用索引或名称来访问管道的步骤：

```python
pipe.steps[0]  # 按索引访问
pipe[0]  # 等同于上述操作
pipe['reduce_dim']  # 按名称访问
```

你还可以使用 `make_pipeline` 函数作为构建管道的简写：

```python
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import Binarizer

make_pipeline(Binarizer(), MultinomialNB())
```

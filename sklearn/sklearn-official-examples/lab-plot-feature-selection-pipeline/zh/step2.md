# 构建管道

现在我们将构建一个由两个步骤组成的管道：特征选择和支持向量机（SVM）分类。我们将使用Scikit-learn的`SelectKBest`函数进行特征选择，并使用Scikit-learn的`LinearSVC`函数进行SVM分类。`SelectKBest`函数基于`f_classif`方法选择`k`个最具信息量的特征，该方法计算每个特征与目标变量之间的方差分析F值。在这个例子中，我们将`k`设置为3。

```python
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

anova_filter = SelectKBest(f_classif, k=3)
clf = LinearSVC(dual="auto")
anova_svm = make_pipeline(anova_filter, clf)
```

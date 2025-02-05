# 特征联合 - 复合特征空间

`FeatureUnion` 类用于将多个变换器对象组合成一个新的变换器，该变换器会合并它们的输出。当你想要对数据的不同特征应用不同的变换时，这很有用，例如分别对文本、浮点数和日期进行预处理。这些变换器会并行应用，并且它们输出的特征矩阵会并排连接成一个更大的矩阵。以下是一个示例：

```python
from sklearn.pipeline import FeatureUnion
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA

estimators = [('linear_pca', PCA()), ('kernel_pca', KernelPCA())]
combined = FeatureUnion(estimators)
```

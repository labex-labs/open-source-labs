# FeatureUnion - Composite Feature Spaces

The `FeatureUnion` class is used to combine multiple transformer objects into a new transformer that combines their output. This is useful when you want to apply different transformations to different features of the data, such as preprocessing text, floats, and dates separately. The transformers are applied in parallel, and the feature matrices they output are concatenated side-by-side into a larger matrix. Here is an example:

```python
from sklearn.pipeline import FeatureUnion
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA

estimators = [('linear_pca', PCA()), ('kernel_pca', KernelPCA())]
combined = FeatureUnion(estimators)
```

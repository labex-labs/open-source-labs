# 创建回归器

我们创建两个回归器：主成分回归（PCR）和偏最小二乘回归（PLS）。为了便于说明，我们将主成分数量设置为 1。在将数据输入到 PCR 的主成分分析（PCA）步骤之前，按照良好实践的建议，我们首先对其进行标准化。PLS 估计器具有内置的缩放功能。

```python
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import PLSRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=rng)

pcr = make_pipeline(StandardScaler(), PCA(n_components=1), LinearRegression())
pcr.fit(X_train, y_train)
pca = pcr.named_steps["pca"]  # retrieve the PCA step of the pipeline

pls = PLSRegression(n_components=1)
pls.fit(X_train, y_train)
```

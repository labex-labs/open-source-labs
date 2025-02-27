# 回帰モデルの作成

PCR と PLS の 2 つの回帰モデルを作成します。この例では、主成分数を 1 に設定します。PCR の PCA ステップにデータを入力する前に、一般的な手法で推奨されているように、まずデータを標準化します。PLS 推定器には、スケーリング機能が組み込まれています。

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

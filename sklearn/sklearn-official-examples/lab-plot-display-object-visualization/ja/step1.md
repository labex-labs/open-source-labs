# データの読み込みとモデルの学習

この例では、OpenMLからの輸血サービスセンターのデータセットを使用します。目的は、個人が献血したかどうかです。まず、データを学習用とテスト用のデータセットに分割し、その後、ロジスティック回帰モデルを学習用データセットでフィットさせます。

```python
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X, y = fetch_openml(data_id=1464, return_X_y=True, parser="pandas")
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)

clf = make_pipeline(StandardScaler(), LogisticRegression(random_state=0))
clf.fit(X_train, y_train)
```

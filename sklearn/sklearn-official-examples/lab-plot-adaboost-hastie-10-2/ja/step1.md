# データとベースラインモデルの準備

まず、Hastie他2009年の例10.2で使用される二値分類データセットを生成します。次に、AdaBoost分類器のハイパーパラメータを設定します。データを訓練用とテスト用に分割します。その後、ベースライン分類器である`depth=9`の`DecisionTreeClassifier`と`depth=1`の「ハズレ木」`DecisionTreeClassifier`を訓練し、テストエラーを計算します。

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

X, y = datasets.make_hastie_10_2(n_samples=12_000, random_state=1)

n_estimators = 400
learning_rate = 1.0

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=2_000, shuffle=False
)

dt_stump = DecisionTreeClassifier(max_depth=1, min_samples_leaf=1)
dt_stump.fit(X_train, y_train)
dt_stump_err = 1.0 - dt_stump.score(X_test, y_test)

dt = DecisionTreeClassifier(max_depth=9, min_samples_leaf=1)
dt.fit(X_train, y_train)
dt_err = 1.0 - dt.score(X_test, y_test)
```

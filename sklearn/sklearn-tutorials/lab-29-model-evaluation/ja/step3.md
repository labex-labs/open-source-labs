# メトリック関数

scikit - learnの`metrics`モジュールは、特定の目的で予測誤差を評価するためのいくつかの関数を実装しています。これらの関数は、モデルによって行われる予測の品質を計算するために使用できます。

以下は、`metrics`モジュールの`accuracy_score`関数を使用する例です。

```python
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = LogisticRegression()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```

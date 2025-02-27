# マルチラベル分類

#### 問題の説明

マルチラベル分類は、各サンプルに複数のラベルを割り当てることができる分類タスクです。各サンプルが持ち得るラベルの数は 2 を超えます。

#### ターゲット形式

マルチラベルターゲットの有効な表現は、2 次元行列で、各行がサンプルを表し、各列がクラスを表します。値が 1 はサンプルにラベルが存在することを示し、0 または -1 は存在しないことを示します。

#### 例

make_classification 関数を使ってマルチラベル分類問題を作成しましょう。

```python
from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier

# Generate a multilabel classification problem
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, random_state=0)
y = y.reshape(-1, 1)

# Fit a multioutput random forest classifier
model = MultiOutputClassifier(RandomForestClassifier())
model.fit(X, y)

# Make predictions
predictions = model.predict(X)
print(predictions)
```

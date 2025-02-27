# 多クラス分類

#### 問題の説明

多クラス分類は、2 クラス以上の分類タスクです。各サンプルはただ 1 つのクラスに割り当てられます。

#### ターゲット形式

多クラスターゲットの有効な表現は、2 つ以上の離散値を含む 1 次元または列ベクトルです。

#### 例

多クラス分類を示すために、Iris データセットを使いましょう。

```python
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier

# Load the Iris dataset
X, y = datasets.load_iris(return_X_y=True)

# Fit a logistic regression model using OneVsRestClassifier
model = OneVsRestClassifier(LogisticRegression())
model.fit(X, y)

# Make predictions
predictions = model.predict(X)
print(predictions)
```

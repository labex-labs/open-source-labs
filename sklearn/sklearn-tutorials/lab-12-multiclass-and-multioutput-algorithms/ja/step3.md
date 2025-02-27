# 多クラス多出力分類

#### 問題の説明

多クラス多出力分類は、マルチタスク分類とも呼ばれ、各サンプルに対して複数の非二値特性を予測します。各特性は 2 クラス以上を持つことができます。

#### ターゲット形式

多クラス多出力ターゲットの有効な表現は、密度行列で、各行がサンプルを表し、各列が異なる特性またはクラスを表します。

#### 例

make_classification 関数を使って多クラス多出力分類問題を作成しましょう。

```python
from sklearn.datasets import make_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.svm import SVC

# Generate a multiclass-multioutput classification problem
X, y = make_classification(n_samples=100, n_features=10, n_informative=5, n_classes=3, random_state=0)

# Fit a multioutput support vector classifier
model = MultiOutputClassifier(SVC())
model.fit(X, y)

# Make predictions
predictions = model.predict(X)
print(predictions)
```

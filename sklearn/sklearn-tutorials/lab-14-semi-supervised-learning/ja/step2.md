# Self Training

#### Self Training アルゴリズムの概要

Self Training アルゴリズムは、Yarowsky のアルゴリズムに基づいています。このアルゴリズムは、教師付き分類器を、未ラベル付きデータから学習することで半教師あり分類器として機能させます。このアルゴリズムは、ラベル付きデータと未ラベル付きデータの両方で教師付き分類器を反復的に訓練し、その後、未ラベル付きデータに対する予測を使って、これらのサンプルのサブセットをラベル付きデータに追加します。すべてのサンプルにラベルが付くか、反復で新しいサンプルが選択されなくなるまで、アルゴリズムは反復を続けます。

#### scikit-learn での Self Training の使用

scikit-learn では、Self Training アルゴリズムは `SelfTrainingClassifier` クラスに実装されています。このアルゴリズムを使用するには、`predict_proba` メソッドを実装する教師付き分類器を提供する必要があります。Self Training アルゴリズムを使用する方法の例を以下に示します。

```python
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.linear_model import LogisticRegression

# ロジスティック回帰分類器を作成
classifier = LogisticRegression()

# ロジスティック回帰分類器をベース分類器とした自己訓練分類器を作成
self_training_classifier = SelfTrainingClassifier(classifier)

# 自己訓練分類器をラベル付きデータと未ラベル付きデータで訓練
self_training_classifier.fit(X_labeled, y_labeled, X_unlabeled)

# 新しいサンプルのラベルを予測
y_pred = self_training_classifier.predict(X_test)
```

上記の例では、`X_labeled` と `y_labeled` はラベル付きデータ、`X_unlabeled` は未ラベル付きデータ、`X_test` は予測対象の新しいサンプルです。

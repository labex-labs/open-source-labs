# ラベル伝播

#### ラベル伝播アルゴリズムの概要

ラベル伝播は、半教師ありグラフ推論アルゴリズムの一種です。入力データセットのすべての項目に対して類似度グラフを構築し、このグラフを使って、ラベル付きデータから未ラベル付きデータにラベルを伝播させます。ラベル伝播は分類タスクに使用でき、データを別の次元空間に射影するためのカーネル手法をサポートします。

#### scikit-learn でのラベル伝播の使用

scikit-learn では、2 つのラベル伝播モデルが利用可能です。`LabelPropagation` と `LabelSpreading` です。両方のモデルは類似度グラフを構築し、ラベルを伝播させます。ラベル伝播を使用する方法の例を以下に示します。

```python
from sklearn.semi_supervised import LabelPropagation

# ラベル伝播モデルを作成
label_propagation = LabelPropagation()

# ラベル付きデータでラベル伝播モデルを訓練
label_propagation.fit(X_labeled, y_labeled)

# 新しいサンプルのラベルを予測
y_pred = label_propagation.predict(X_test)
```

上記の例では、`X_labeled` と `y_labeled` はラベル付きデータであり、`X_test` は予測対象の新しいサンプルです。

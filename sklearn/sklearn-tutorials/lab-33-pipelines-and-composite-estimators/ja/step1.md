# パイプライン - 推定器のチェーニング

scikit-learn の `Pipeline` クラスは、複数の推定器を 1 つにチェーニングするために使用されます。これにより、データに対して一度の `fit` と `predict` 呼び出しで、推定器の一連の全体を適合させることができます。また、共通のパラメータ選択も可能で、クロスバリデーションにおけるデータの漏洩を回避するのに役立ちます。

パイプラインを作成するには、`(キー, 値)` のペアのリストを提供する必要があります。ここで、`キー` は各ステップを識別するための文字列で、`値` は推定器オブジェクトです。以下は、PCA 変換器と SVM 分類器を持つパイプラインを作成する例です：

```python
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA

estimators = [('reduce_dim', PCA()), ('clf', SVC())]
pipe = Pipeline(estimators)
```

パイプラインのステップには、インデックスまたは名前を使ってアクセスできます：

```python
pipe.steps[0]  # インデックスでアクセス
pipe[0]  # 上記と同等
pipe['reduce_dim']  # 名前でアクセス
```

また、`make_pipeline` 関数を使って、パイプラインの構築を省略形で行うこともできます：

```python
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import Binarizer

make_pipeline(Binarizer(), MultinomialNB())
```

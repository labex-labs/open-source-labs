# 特徴量抽出

テキストデータを特徴量ベクトルとして表現するには、単語袋表現を使用できます。この表現では、訓練セット内の各単語に固定された整数 ID を割り当て、各文書内の各単語の出現回数をカウントします。scikit-learn の `CountVectorizer` を使用して、これらの特徴量ベクトルを抽出できます。

```python
from sklearn.feature_extraction.text import CountVectorizer

# 特徴量ベクトルを抽出する
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
```

これで特徴量ベクトルが抽出されました。これらを使ってモデルの学習に使用できます。

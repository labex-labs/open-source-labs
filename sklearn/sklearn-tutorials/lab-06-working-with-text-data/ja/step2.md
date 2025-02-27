# テキストデータの前処理

機械学習にテキストデータを使用する前に、前処理が必要です。これには、句読点を削除したり、すべてのテキストを小文字に変換したり、テキストを個々の単語にトークナイズしたりなど、いくつかのステップが含まれます。scikit-learn の `CountVectorizer` と `TfidfTransformer` を使用して、これらの前処理ステップを実行できます。

```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# テキストデータを前処理する
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
```

これで、テキストデータの前処理が完了し、特徴量抽出の準備が整いました。

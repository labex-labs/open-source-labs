# モデルの学習

特徴量ベクトルができたので、テキストデータを分類するモデルを学習させることができます。この例では、テキスト分類に人気のあるアルゴリズムである多項式ナイーブベイズアルゴリズムを使用します。

```python
from sklearn.naive_bayes import MultinomialNB

# モデルを学習させる
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)
```

これでモデルの学習が完了し、予測の準備が整いました。

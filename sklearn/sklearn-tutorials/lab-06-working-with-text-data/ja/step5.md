# モデルの評価

モデルの性能を評価するには、ホールドアウトテストセットを使用できます。訓練セットと同じプロセスを使ってテストセットを読み込めます。

```python
twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)
```

これで、テストセットの前処理と特徴量ベクトルの抽出ができます。

```python
X_test_counts = count_vect.transform(twenty_test.data)
X_test_tfidf = tfidf_transformer.transform(X_test_counts)
```

最後に、学習済みのモデルを使ってテストセットに対して予測を行い、精度を計算できます。

```python
predicted = clf.predict(X_test_tfidf)
accuracy = np.mean(predicted == twenty_test.target)
```

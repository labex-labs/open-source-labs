# ベクトル化器を設定し、テストセットを分離する

```python
# ベクトル化器を作成し、機能の数を合理的な最大値に制限する
vectorizer = HashingVectorizer(decode_error="ignore", n_features=2**18, alternate_sign=False)

# 解析済みのルイト社のSGMLファイルの反復処理。
data_stream = stream_reuters_documents()

# 「acq」クラスとその他のすべてのクラスの間の2値分類を学習する。
# 「acq」はルイト社のファイルにほぼ均等に分布しているため選択された。他のデータセットの場合、正例の現実的な割合を持つテストセットを作成することに注意する必要がある。
all_classes = np.array([0, 1])
positive_class = "acq"

# ここには、`partial_fit` メソッドをサポートするいくつかの分類器がある
partial_fit_classifiers = {
    "SGD": SGDClassifier(max_iter=5),
    "Perceptron": Perceptron(),
    "NB Multinomial": MultinomialNB(alpha=0.01),
    "Passive-Aggressive": PassiveAggressiveClassifier(),
}

# テストデータの統計
test_stats = {"n_test": 0, "n_test_pos": 0}

# まず、精度を推定するためにいくつかのサンプルを分離する
n_test_documents = 1000
X_test_text, y_test = get_minibatch(data_stream, 1000)
X_test = vectorizer.transform(X_test_text)
test_stats["n_test"] += len(y_test)
test_stats["n_test_pos"] += sum(y_test)
print("Test set is %d documents (%d positive)" % (len(y_test), sum(y_test)))
```

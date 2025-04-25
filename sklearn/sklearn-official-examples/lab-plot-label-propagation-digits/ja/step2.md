# 半教師あり学習用のデータの準備

340 個のサンプルを選択し、これらのサンプルのうち 40 個のみに既知のラベルを関連付けます。ラベルが不明であると想定される他の 300 個のサンプルのインデックスを保存します。その後、ラベルをシャッフルして、ラベルのないサンプルを -1 でマークします。

```python
X = digits.data[indices[:340]]
y = digits.target[indices[:340]]

n_total_samples = len(y)
n_labeled_points = 40

indices = np.arange(n_total_samples)

unlabeled_set = indices[n_labeled_points:]

y_train = np.copy(y)
y_train[unlabeled_set] = -1
```

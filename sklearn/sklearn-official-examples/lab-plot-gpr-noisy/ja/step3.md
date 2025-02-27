# ノイズの追加

このステップでは、生成したデータにいくらかのノイズを追加して、より現実的な学習データセットを作成します。

```python
rng = np.random.RandomState(0)
X_train = rng.uniform(0, 5, size=20).reshape(-1, 1)
y_train = target_generator(X_train, add_noise=True)
```

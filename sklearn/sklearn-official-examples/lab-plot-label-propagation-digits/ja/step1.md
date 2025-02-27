# データの読み込みとシャッフル

まず、数字データセットを読み込み、データをランダムにシャッフルします。

```python
digits = datasets.load_digits()
rng = np.random.RandomState(2)
indices = np.arange(len(digits.data))
rng.shuffle(indices)
```

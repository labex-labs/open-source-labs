# パラメータ空間の定義

探索するハイパーパラメータとそれぞれの値を含む辞書`param_dist`を定義します。ハイパーパラメータは`max_depth`、`max_features`、`min_samples_split`、`bootstrap`、および`criterion`です。`max_features`と`min_samples_split`の探索範囲は、`scipy.stats`モジュールの`randint`関数を使って定義されます。パラメータ空間を定義するコードは以下の通りです：

```python
param_dist = {
    "max_depth": [3, None],
    "max_features": randint(1, 6),
    "min_samples_split": randint(2, 11),
    "bootstrap": [True, False],
    "criterion": ["gini", "entropy"],
}
```

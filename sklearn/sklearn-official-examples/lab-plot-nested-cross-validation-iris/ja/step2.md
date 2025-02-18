# ハイパーパラメータの定義

次に、サポートベクター分類器の最適化対象となるハイパーパラメータを定義します。この場合、コストパラメータ `C` とカーネル係数 `gamma` を最適化します。

```python
# Set up possible values of parameters to optimize over
p_grid = {"C": [1, 10, 100], "gamma": [0.01, 0.1]}
```

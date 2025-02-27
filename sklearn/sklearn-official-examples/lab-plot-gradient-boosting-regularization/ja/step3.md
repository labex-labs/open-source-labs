# パラメータの定義

勾配ブースティング分類器のパラメータを定義します。以下のパラメータを使用します。

- n_estimators: 実行するブースティングステージの数
- max_leaf_nodes: 各木の最大葉ノード数
- max_depth: 木の最大深さ
- random_state: 一貫性のための乱数シード
- min_samples_split: 内部ノードを分割するために必要な最小サンプル数

```python
original_params = {
    "n_estimators": 400,
    "max_leaf_nodes": 4,
    "max_depth": None,
    "random_state": 2,
    "min_samples_split": 5,
}
```

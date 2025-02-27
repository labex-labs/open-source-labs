# サンプルのグループに共通するノードを特定する

サンプルのグループに対して、`decision_path`メソッドと指標行列を密集配列に変換するための`toarray`メソッドを使って、サンプルが通過する共通のノードを特定することができます。

```python
sample_ids = [0, 1]
# 両方のサンプルが通過するノードを示すブール配列
common_nodes = node_indicator.toarray()[sample_ids].sum(axis=0) == len(sample_ids)
# 配列内の位置を使ってノードIDを取得する
common_node_id = np.arange(n_nodes)[common_nodes]

print(
    "\n以下のサンプル{samples}は木構造においてノード{nodes}を共有しています。".format(
        samples=sample_ids, nodes=common_node_id
    )
)
print("これは全ノードの{prop}%です。".format(prop=100 * len(common_node_id) / n_nodes))
```

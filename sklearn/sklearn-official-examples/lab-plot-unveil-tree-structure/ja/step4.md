# 決定経路と葉ノードを取得する

`decision_path`メソッドを使って、関心のあるサンプルの決定経路を取得することができます。このメソッドは、指標行列を出力し、それを使って関心のあるサンプルが通過するノードを取得できます。関心のあるサンプルが到達する葉の ID は、`apply`メソッドで取得できます。これは、各関心のあるサンプルが到達する葉のノード ID の配列を返します。葉の ID と`decision_path`を使って、サンプルまたはサンプルのグループを予測するために使用された分割条件を取得できます。以下は、1 つのサンプルの決定経路と葉ノードを取得するコードです。

```python
node_indicator = clf.decision_path(X_test)
leaf_id = clf.apply(X_test)

sample_id = 0
# サンプル ID `sample_id` が通過するノードの ID を取得する、つまり行 `sample_id`
node_index = node_indicator.indices[
    node_indicator.indptr[sample_id] : node_indicator.indptr[sample_id + 1]
]

print("サンプル{id}を予測するために使用されるルール:\n".format(id=sample_id))
for node_id in node_index:
    # 葉ノードの場合は次のノードに進む
    if leaf_id[sample_id] == node_id:
        continue

    # サンプル 0 の分割特徴量の値が閾値以下かどうかを確認する
    if X_test[sample_id, feature[node_id]] <= threshold[node_id]:
        threshold_sign = "<="
    else:
        threshold_sign = ">"

    print(
        "決定ノード{node} : (X_test[{sample}, {feature}] = {value}) "
        "{inequality} {threshold})".format(
            node=node_id,
            sample=sample_id,
            feature=feature[node_id],
            value=X_test[sample_id, feature[node_id]],
            inequality=threshold_sign,
            threshold=threshold[node_id],
        )
    )
```

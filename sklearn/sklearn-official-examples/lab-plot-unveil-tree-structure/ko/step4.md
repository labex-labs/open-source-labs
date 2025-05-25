# 의사결정 경로 및 잎 노드 검색

`decision_path` 메서드를 사용하여 관심 있는 샘플의 의사결정 경로를 검색할 수 있습니다. 이 메서드는 관심 있는 샘플이 거치는 노드를 검색할 수 있도록 지표 행렬을 출력합니다. 관심 있는 샘플이 도달한 잎 노드 ID 는 `apply` 메서드를 사용하여 얻을 수 있습니다. 이 메서드는 각 관심 샘플이 도달한 잎 노드의 ID 배열을 반환합니다. 잎 노드 ID 와 `decision_path`를 사용하여 샘플 또는 샘플 그룹을 예측하는 데 사용된 분할 조건을 얻을 수 있습니다. 아래는 한 샘플에 대한 의사결정 경로 및 잎 노드를 검색하는 코드입니다.

```python
node_indicator = clf.decision_path(X_test)
leaf_id = clf.apply(X_test)

sample_id = 0
# 샘플 `sample_id` 가 거치는 노드의 ID 를 얻습니다 (즉, 행 `sample_id`)
node_index = node_indicator.indices[
    node_indicator.indptr[sample_id] : node_indicator.indptr[sample_id + 1]
]

print("샘플 {id}를 예측하는 데 사용된 규칙:\n".format(id=sample_id))
for node_id in node_index:
    # 잎 노드이면 다음 노드로 이동합니다.
    if leaf_id[sample_id] == node_id:
        continue

    # 샘플 0 의 분할 특성 값이 임계값보다 작은지 확인합니다.
    if X_test[sample_id, feature[node_id]] <= threshold[node_id]:
        threshold_sign = "<="
    else:
        threshold_sign = ">"

    print(
        "의사결정 노드 {node} : (X_test[{sample}, {feature}] = {value}) "
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

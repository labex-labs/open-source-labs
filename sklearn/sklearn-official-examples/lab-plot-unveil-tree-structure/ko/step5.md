# 여러 샘플의 공통 노드 확인

여러 샘플에 대해 `decision_path` 메서드와 `toarray` 메서드를 사용하여 지표 행렬을 밀집 배열로 변환하여 샘플들이 거치는 공통 노드를 확인할 수 있습니다.

```python
sample_ids = [0, 1]
# 두 샘플 모두 거치는 노드를 나타내는 불리언 배열
common_nodes = node_indicator.toarray()[sample_ids].sum(axis=0) == len(sample_ids)
# 배열 내 위치를 사용하여 노드 ID 를 얻습니다.
common_node_id = np.arange(n_nodes)[common_nodes]

print(
    "\n다음 샘플 {samples}는 트리에서 노드 {nodes}를 공유합니다.".format(
        samples=sample_ids, nodes=common_node_id
    )
)
print("이는 모든 노드의 {prop}%입니다.".format(prop=100 * len(common_node_id) / n_nodes))
```

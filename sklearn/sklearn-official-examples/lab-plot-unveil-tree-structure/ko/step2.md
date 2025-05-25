# 이진 트리 구조 분석

의사결정 트리 분류기에는 `tree_`라는 속성이 있습니다. 이 속성을 통해 노드의 총 개수인 `node_count`와 트리의 최대 깊이인 `max_depth`와 같은 저수준 속성에 접근할 수 있습니다. 또한, 여러 개의 병렬 배열로 표현되는 전체 이진 트리 구조를 저장합니다. 이러한 배열을 사용하여 트리 구조를 탐색하여 각 노드의 깊이와 노드가 잎 노드인지 여부와 같은 다양한 속성을 계산할 수 있습니다. 아래는 이러한 속성을 계산하는 코드입니다.

```python
import numpy as np

n_nodes = clf.tree_.node_count
children_left = clf.tree_.children_left
children_right = clf.tree_.children_right
feature = clf.tree_.feature
threshold = clf.tree_.threshold

node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
is_leaves = np.zeros(shape=n_nodes, dtype=bool)
stack = [(0, 0)]  # 루트 노드 ID(0) 와 깊이 (0) 로 시작
while len(stack) > 0:
    # `pop` 을 통해 각 노드는 한 번만 방문되도록 합니다.
    node_id, depth = stack.pop()
    node_depth[node_id] = depth

    # 노드의 왼쪽 및 오른쪽 자식이 같지 않으면 분할 노드입니다.
    is_split_node = children_left[node_id] != children_right[node_id]
    # 분할 노드인 경우 왼쪽 및 오른쪽 자식과 깊이를 `stack` 에 추가하여 반복할 수 있도록 합니다.
    if is_split_node:
        stack.append((children_left[node_id], depth + 1))
        stack.append((children_right[node_id], depth + 1))
    else:
        is_leaves[node_id] = True

print(
    "이진 트리 구조에는 {n}개의 노드가 있으며 다음과 같은 트리 구조를 갖습니다:\n".format(n=n_nodes)
)
for i in range(n_nodes):
    if is_leaves[i]:
        print(
            "{space}node={node}는 잎 노드입니다.".format(
                space=node_depth[i] * "\t", node=i
            )
        )
    else:
        print(
            "{space}node={node}는 분할 노드입니다: "
            "X[:, {feature}] <= {threshold}이면 노드 {left}로, "
            "그렇지 않으면 노드 {right}로 이동합니다.".format(
                space=node_depth[i] * "\t",
                node=i,
                left=children_left[i],
                feature=feature[i],
                threshold=threshold[i],
                right=children_right[i],
            )
        )
```

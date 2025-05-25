# 매개변수 정의

Gradient Boosting Classifier 의 매개변수를 정의합니다. 다음 매개변수를 사용합니다.

- n_estimators: 부스팅 단계 수
- max_leaf_nodes: 각 트리의 최대 리프 노드 수
- max_depth: 트리의 최대 깊이
- random_state: 일관성을 위한 난수 시드
- min_samples_split: 내부 노드를 분할하는 데 필요한 최소 샘플 수

```python
original_params = {
    "n_estimators": 400,
    "max_leaf_nodes": 4,
    "max_depth": None,
    "random_state": 2,
    "min_samples_split": 5,
}
```

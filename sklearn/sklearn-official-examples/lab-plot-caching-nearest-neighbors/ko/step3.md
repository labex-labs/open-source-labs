# 최근접 이웃 그래프 계산

이 단계에서는 KNeighborsTransformer 를 사용하여 최근접 이웃 그래프를 계산합니다.

```python
# 변환기는 그리드 검색에서 필요한 최대 이웃 수를 사용하여 최근접 이웃 그래프를 계산합니다. 분류기 모델은 자체 n_neighbors 매개변수에 따라 필요에 따라 최근접 이웃 그래프를 필터링합니다.
graph_model = KNeighborsTransformer(n_neighbors=max(n_neighbors_list), mode="distance")
```

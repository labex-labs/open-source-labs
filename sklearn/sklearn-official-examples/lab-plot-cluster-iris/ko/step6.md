# 군집화 평가

K-Means 군집화 알고리즘의 성능을 평가하기 위해 관성 (Inertia) 점수를 계산할 수 있습니다. 관성 점수는 각 데이터 포인트와 할당된 클러스터 중심 사이의 거리의 합을 측정합니다. 관성 점수가 낮을수록 군집화가 더 좋습니다.

```python
print("Inertia Score:", kmeans.inertia_)
```

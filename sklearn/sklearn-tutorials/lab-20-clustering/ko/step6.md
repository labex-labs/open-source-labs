# 군집 평가

군집 결과를 평가하기 위해 군집의 관성 (inertia) 을 계산할 수 있습니다. 관성은 샘플과 가장 가까운 군집 중심까지의 제곱 거리의 합을 나타냅니다.

```python
# 군집의 관성 계산
inertia = kmeans.inertia_
print("Inertia:", inertia)
```

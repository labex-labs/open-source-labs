# 데이터 정제

이 단계에서는 `tri.UniformTriRefiner`를 사용하여 데이터를 정제합니다. `refine_field` 메서드를 사용하여 `z` 값을 정제하고 더 높은 해상도의 새로운 Triangulation (삼각 측량) 을 생성합니다.

```python
refiner = tri.UniformTriRefiner(triang)
tri_refi, z_test_refi = refiner.refine_field(z, subdiv=3)
```

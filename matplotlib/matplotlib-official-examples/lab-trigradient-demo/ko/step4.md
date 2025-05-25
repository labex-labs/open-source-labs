# 데이터 세분화

```python
refiner = UniformTriRefiner(triang)
tri_refi, z_test_refi = refiner.refine_field(V, subdiv=3)
```

설명:

- `UniformTriRefiner`는 삼각 측량 (triangulation) 을 세분화하여 더 정확한 플롯을 생성하는 클래스입니다.
- `refiner`는 `UniformTriRefiner` 클래스의 인스턴스입니다.
- `tri_refi`와 `z_test_refi`는 각각 세분화된 삼각 측량과 전위 값입니다.

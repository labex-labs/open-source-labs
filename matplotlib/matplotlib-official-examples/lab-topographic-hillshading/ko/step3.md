# 셀 크기 지정

지형학적으로 정확한 수직 과장 (vertical exaggeration) 이 필요하거나, `vert_exag` 값을 추측하고 싶지 않다면, 그리드의 셀 크기 (즉, `dx` 및 `dy` 매개변수) 를 지정해야 합니다. 그렇지 않으면, 지정하는 모든 `vert_exag` 값은 입력 데이터의 그리드 간격에 상대적입니다. 이 단계에서는 미터 단위의 `dx` 및 `dy` 값을 계산합니다.

```python
dy = 111200 * dy
dx = 111200 * dx * np.cos(np.radians(dem['ymin']))
```

# 속성 사이클 정의 및 색상 가져오기

다음으로, 속성 사이클을 정의하고 거기에서 색상을 가져와야 합니다.

```python
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']
```

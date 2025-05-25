# 기생 축 조정

기생 축의 위치를 조정해야 합니다. `new_fixed_axis()` 함수는 플롯의 오른쪽에 새로운 y 축을 생성하는 데 사용됩니다. `toggle()` 함수는 오른쪽 y 축의 모든 눈금과 레이블을 켜는 데 사용됩니다.

```python
par2.axis["right"] = par2.new_fixed_axis(loc="right", offset=(60, 0))

par1.axis["right"].toggle(all=True)
par2.axis["right"].toggle(all=True)
```

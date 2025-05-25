# 첫 번째 기생 축의 오른쪽 y 축 표시

`par1.axis["right"].set_visible(True)` 메서드를 사용하여 첫 번째 기생 축의 오른쪽 y 축을 표시합니다. 또한 오른쪽 y 축의 눈금 레이블과 레이블을 표시하기 위해 `par1.axis["right"].major_ticklabels.set_visible(True)` 및 `par1.axis["right"].label.set_visible(True)`을 설정합니다.

```python
par1.axis["right"].set_visible(True)
par1.axis["right"].major_ticklabels.set_visible(True)
par1.axis["right"].label.set_visible(True)
```

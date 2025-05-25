# 막대 차트 매개변수 정의

다음 단계는 막대 차트의 매개변수를 정의하는 것입니다. 그룹의 x 위치, 막대의 너비, x-눈금 레이블을 정의합니다.

```python
ind = np.arange(N)    # the x locations for the groups
width = 0.35         # the width of the bars
ax.set_xticks(ind + width / 2, labels=['G1', 'G2', 'G3', 'G4', 'G5'])
```

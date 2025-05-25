# 중앙 서브플롯에 레이블 추가

이것이 기본 3D 뷰 평면 플롯임을 나타내기 위해 중앙 서브플롯에 레이블을 추가합니다.

```python
label = 'mplot3d primary view planes\n' + 'ax.view_init(elev, azim, roll)'
annotate_axes(axd['L'], label, fontsize=18)
axd['L'].set_axis_off()
```

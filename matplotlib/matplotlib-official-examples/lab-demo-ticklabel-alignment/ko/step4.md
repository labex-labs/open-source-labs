# 틱 레이블 정렬 조정

마지막으로, `set_ha` 및 `set_va` 메서드를 사용하여 틱 레이블의 수평 및 수직 정렬을 조정할 수 있습니다.

```python
ax.axis["left"].major_ticklabels.set_ha("center")
ax.axis["bottom"].major_ticklabels.set_va("top")
```

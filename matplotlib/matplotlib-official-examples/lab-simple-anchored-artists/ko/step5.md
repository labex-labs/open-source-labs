# 크기 막대 추가

데이터 좌표에서 길이가 0.1 인 수평 막대를 그리고, 그 아래에 고정된 레이블을 표시합니다.

```python
asb = AnchoredSizeBar(ax.transData,
                      0.1,
                      r"1$^{\prime}$",
                      loc='lower center',
                      pad=0.1, borderpad=0.5, sep=5,
                      frameon=False)
ax.add_artist(asb)
```

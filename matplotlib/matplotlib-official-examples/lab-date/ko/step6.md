# 간결한 포맷터를 사용하여 눈금 레이블 형식 지정

두 번째 서브플롯의 눈금 레이블을 간결한 포맷터 (concise formatter) 를 사용하여 형식 지정합니다.

```python
ax = axs[1]
ax.set_title('ConciseFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
```

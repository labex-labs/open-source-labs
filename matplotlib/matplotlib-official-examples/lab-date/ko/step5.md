# 기본 포맷터를 사용하여 눈금 레이블 형식 지정

첫 번째 서브플롯의 눈금 레이블을 기본 포맷터 (default formatter) 를 사용하여 형식 지정합니다.

```python
ax = axs[0]
ax.set_title('DefaultFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
```

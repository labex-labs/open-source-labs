# 수동으로 눈금 레이블 형식 지정

세 번째 서브플롯의 눈금 레이블을 `DateFormatter`를 사용하여 수동으로 형식 지정하며, `datetime.date.strftime`에 문서화된 형식 문자열을 사용하여 날짜 형식을 지정합니다.

```python
ax = axs[2]
ax.set_title('Manual DateFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
for label in ax.get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')
```

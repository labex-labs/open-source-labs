# 플롯 서식 지정

이제 x 축 및 y 축 레이블을 추가하고, x 축 주요 로케이터 (locator) 및 포맷터 (formatter) 를 설정하고, y 축 및 스파인 (spine) 을 제거하여 플롯의 서식을 지정합니다. 다음은 플롯의 서식을 지정하는 코드입니다.

```python
# format x-axis with 4-month intervals
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

# remove y-axis and spines
ax.yaxis.set_visible(False)
ax.spines[["left", "top", "right"]].set_visible(False)

ax.margins(y=0.1)
plt.show()
```

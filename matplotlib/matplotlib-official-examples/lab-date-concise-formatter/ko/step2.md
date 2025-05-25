# 간결한 날짜 형식 지정자

다음으로, `~.dates.ConciseDateFormatter`와 그 출력을 살펴보겠습니다. 간결한 날짜 형식 지정자를 사용하여 새로운 플롯을 만들고, 이것이 기본 형식 지정자와 어떻게 다른지 확인합니다.

```python
fig, axs = plt.subplots(3, 1, layout='constrained', figsize=(6, 6))
for nn, ax in enumerate(axs):
    locator = mdates.AutoDateLocator(minticks=3, maxticks=7)
    formatter = mdates.ConciseDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
axs[0].set_title('Concise Date Formatter')
plt.show()
```

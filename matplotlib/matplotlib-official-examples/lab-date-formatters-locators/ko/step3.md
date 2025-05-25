# 그래프 플로팅 (Plotting the Graphs)

이제 그래프를 생성할 수 있습니다. 로케이터와 포맷터를 별도로 시연하기 위해 두 개의 서브플롯 (subplots) 을 생성합니다. 각 로케이터와 포맷터에 대해, X 축에 어떤 영향을 미치는지 보여주는 그래프를 플롯합니다. 이를 위해 `plot_axis` 함수를 사용합니다. 이 함수는 스파인 (spines), 틱 파라미터 (tick parameters), 제한 (limits) 과 같이 각 축에 대한 공통 매개변수를 설정합니다. 또한 X 축에 대한 로케이터와 포맷터를 설정합니다.

```python
def plot_axis(ax, locator=None, xmax='2002-02-01', fmt=None, formatter=None):
    ax.spines[['left', 'right', 'top']].set_visible(False)
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.tick_params(which='major', width=1.00, length=5)
    ax.tick_params(which='minor', width=0.75, length=2.5)
    ax.set_xlim(np.datetime64('2000-02-01'), np.datetime64(xmax))
    if locator:
        ax.xaxis.set_major_locator(eval(locator))
        ax.xaxis.set_major_formatter(DateFormatter(fmt))
    else:
        ax.xaxis.set_major_formatter(eval(formatter))
    ax.text(0.0, 0.2, locator or formatter, transform=ax.transAxes,
            fontsize=14, fontname='Monospace', color='tab:blue')


fig, axs = plt.subplots(len(locators), 1, figsize=(8, len(locators) * .8),
                        layout='constrained')
fig.suptitle('Date Locators')
for ax, (locator, xmax, fmt) in zip(axs, locators):
    plot_axis(ax, locator, xmax, fmt)

fig, axs = plt.subplots(len(formatters), 1, figsize=(8, len(formatters) * .8),
                        layout='constrained')
fig.suptitle('Date Formatters')
for ax, fmt in zip(axs, formatters):
    plot_axis(ax, formatter=fmt)
```

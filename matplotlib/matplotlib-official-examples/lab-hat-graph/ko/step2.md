# Hat 그래프 함수 정의

이 단계에서는 Hat 그래프를 생성하는 함수를 정의합니다. 이 함수는 다음과 같은 매개변수를 사용합니다.

- ax: 플롯할 Axes (축).
- xlabels: x 축에 표시될 범주 이름.
- values: 데이터 값. 행은 그룹이고, 열은 범주입니다.
- group_labels: 범례에 표시될 그룹 레이블.

```python
def hat_graph(ax, xlabels, values, group_labels):
    """
    Hat 그래프를 생성합니다.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        플롯할 Axes (축).
    xlabels : list of str
        x 축에 표시될 범주 이름 목록.
    values : (M, N) array-like
        데이터 값.
        행은 그룹 (len(group_labels) == M) 입니다.
        열은 범주 (len(xlabels) == N) 입니다.
    group_labels : list of str
        범례에 표시될 그룹 레이블 목록.
    """

    def label_bars(heights, rects):
        """각 막대 위에 텍스트 레이블을 첨부합니다."""
        for height, rect in zip(heights, rects):
            ax.annotate(f'{height}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 4),  # 4 points vertical offset.
                        textcoords='offset points',
                        ha='center', va='bottom')

    values = np.asarray(values)
    x = np.arange(values.shape[1])
    ax.set_xticks(x, labels=xlabels)
    spacing = 0.3  # hat 그룹 간 간격
    width = (1 - spacing) / values.shape[0]
    heights0 = values[0]
    for i, (heights, group_label) in enumerate(zip(values, group_labels)):
        style = {'fill': False} if i == 0 else {'edgecolor': 'black'}
        rects = ax.bar(x - spacing/2 + i * width, heights - heights0,
                       width, bottom=heights0, label=group_label, **style)
        label_bars(heights, rects)
```

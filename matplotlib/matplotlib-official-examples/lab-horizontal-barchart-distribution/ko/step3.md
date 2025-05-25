# 함수 정의

이제 `results`와 `category_names`를 입력받아 수평 누적 막대 차트 시각화를 생성하는 `survey`라는 함수를 정의합니다.

```python
def survey(results, category_names):
    """
    Parameters
    ----------
    results : dict
        질문 레이블에서 각 범주별 답변 목록으로의 매핑.
        모든 목록이 동일한 수의 항목을 포함하고 *category_names*의 길이와 일치한다고 가정합니다.
    category_names : list of str
        범주 레이블.
    """
    # 결과를 numpy 배열로 변환
    labels = list(results.keys())
    data = np.array(list(results.values()))

    # 수평 누적을 위해 데이터의 누적 합계 계산
    data_cum = data.cumsum(axis=1)

    # 범주 색상 정의
    category_colors = plt.colormaps['RdYlGn'](
        np.linspace(0.15, 0.85, data.shape[1]))

    # 플롯 생성 및 축 속성 설정
    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    # 누적 막대 생성 및 막대 레이블 추가
    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)
        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color)

    # 범례 추가
    ax.legend(ncols=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax
```

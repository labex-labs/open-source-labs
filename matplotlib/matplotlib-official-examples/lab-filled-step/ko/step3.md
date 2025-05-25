# 스택 히스토그램 함수 정의

스택 히스토그램을 생성하는 함수를 정의합니다. 이 함수는 다음과 같은 매개변수를 사용합니다.

- `ax`: 아티스트 (artist) 를 추가할 축 (axes)
- `stacked_data`: (M, N) 모양의 배열. 첫 번째 차원은 행별로 히스토그램을 계산하기 위해 반복됩니다.
- `sty_cycle`: 각 세트에 적용할 스타일인 Cycler 또는 dict 의 연산 가능 객체
- `bottoms`: 배열, 기본값: 0, 하단의 초기 위치.
- `hist_func`: 호출 가능 객체, 선택 사항. 시그니처 `bin_vals, bin_edges = f(data)`가 있어야 합니다. `bin_edges`는 `bin_vals`보다 하나 더 길어야 합니다.
- `labels`: 문자열 목록, 선택 사항, 각 세트의 레이블. 제공되지 않고 stacked_data 가 배열인 경우 'default set {n}'으로 기본 설정됩니다. stacked_data 가 매핑이고 labels 가 None 인 경우 키로 기본 설정됩니다. stacked_data 가 매핑이고 labels 가 제공된 경우 나열된 열만 플롯됩니다.
- `plot_func`: 호출 가능 객체, 선택 사항, 히스토그램을 그리기 위해 호출할 함수. 시그니처 `ret = plot_func(ax, edges, top, bottoms=bottoms, label=label, **kwargs)`가 있어야 합니다.
- `plot_kwargs`: 딕셔너리, 선택 사항, 플로팅 함수에 전달할 추가 키워드 인수. 이는 플로팅 함수에 대한 모든 호출에 대해 동일하며 `sty_cycle`의 값을 재정의합니다.

```python
def stack_hist(ax, stacked_data, sty_cycle, bottoms=None, hist_func=None, labels=None, plot_func=None, plot_kwargs=None):
    """
    매개변수
    ----------
    ax : axes.Axes
        아티스트를 추가할 축

    stacked_data : array 또는 Mapping
        (M, N) 모양의 배열. 첫 번째 차원은 행별로
        히스토그램을 계산하기 위해 반복됩니다.

    sty_cycle : Cycler 또는 dict 의 연산 가능 객체
        각 세트에 적용할 스타일

    bottoms : array, 기본값: 0
        하단의 초기 위치.

    hist_func : callable, 선택 사항
        시그니처 `bin_vals, bin_edges = f(data)`가 있어야 합니다.
        `bin_edges` 는 `bin_vals` 보다 하나 더 길어야 합니다.

    labels : list of str, 선택 사항
        각 세트의 레이블.

        제공되지 않고 stacked data 가 배열인 경우 'default set {n}'으로 기본 설정됩니다.

        *stacked_data*가 매핑이고 *labels*가 None 인 경우 키로 기본 설정됩니다.

        *stacked_data*가 매핑이고 *labels*가 제공된 경우 나열된
        열만 플롯됩니다.

    plot_func : callable, 선택 사항
        히스토그램을 그리기 위해 호출할 함수는 다음 시그니처를 가져야 합니다.

          ret = plot_func(ax, edges, top, bottoms=bottoms,
                          label=label, **kwargs)

    plot_kwargs : dict, 선택 사항
        플로팅 함수에 전달할 추가 키워드 인수.
        이는 플로팅 함수에 대한 모든 호출에 대해 동일하며
        *sty_cycle*의 값을 재정의합니다.

    반환값
    -------
    arts : dict
        레이블을 기준으로 키가 지정된 아티스트의 딕셔너리
    """
    # 기본 binning 함수 처리
    if hist_func is None:
        hist_func = np.histogram

    # 기본 플로팅 함수 처리
    if plot_func is None:
        plot_func = filled_hist

    # 기본값 처리
    if plot_kwargs is None:
        plot_kwargs = {}

    try:
        l_keys = stacked_data.keys()
        label_data = True
        if labels is None:
            labels = l_keys

    except AttributeError:
        label_data = False
        if labels is None:
            labels = itertools.repeat(None)

    if label_data:
        loop_iter = enumerate((stacked_data[lab], lab, s) for lab, s in zip(labels, sty_cycle))
    else:
        loop_iter = enumerate(zip(stacked_data, labels, sty_cycle))

    arts = {}
    for j, (data, label, sty) in loop_iter:
        if label is None:
            label = f'dflt set {j}'
        label = sty.pop('label', label)
        vals, edges = hist_func(data)
        if bottoms is None:
            bottoms = np.zeros_like(vals)
        top = bottoms + vals
        sty.update(plot_kwargs)
        ret = plot_func(ax, edges, top, bottoms=bottoms, label=label, **sty)
        bottoms = top
        arts[label] = ret
    ax.legend(fontsize=10)
    return arts
```

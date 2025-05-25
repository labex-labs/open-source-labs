# 히스토그램 함수 정의

계단형 패치 (stepped patch) 로 히스토그램을 그리는 함수를 정의합니다. 이 함수는 다음과 같은 매개변수를 사용합니다.

- `ax`: 플롯을 그릴 Axes
- `edges`: 각 빈 (bin) 의 왼쪽 가장자리와 마지막 빈의 오른쪽 가장자리를 제공하는 길이 n+1 배열
- `values`: 빈 카운트 또는 값을 나타내는 길이 n 배열
- `bottoms`: float 또는 배열, 선택 사항, 막대의 하단을 나타내는 길이 n 배열. None 인 경우 0 이 사용됩니다.
- `orientation`: 문자열, 선택 사항, 히스토그램의 방향. 'v'(기본값) 는 막대가 양의 y 방향으로 증가합니다.

```python
def filled_hist(ax, edges, values, bottoms=None, orientation='v', **kwargs):
    """
    계단형 패치로 히스토그램을 그립니다.

    매개변수
    ----------
    ax : Axes
        플롯을 그릴 축 (Axes)

    edges : array
        각 빈 (bin) 의 왼쪽 가장자리와
        마지막 빈의 오른쪽 가장자리를 제공하는 길이 n+1 배열.

    values : array
        빈 카운트 또는 값을 나타내는 길이 n 배열

    bottoms : float 또는 array, 선택 사항
        막대의 하단을 나타내는 길이 n 배열.  None 인 경우 0 이 사용됩니다.

    orientation : {'v', 'h'}
       히스토그램의 방향.  'v'(기본값) 는
       막대가 양의 y 방향으로 증가합니다.

    **kwargs
        추가 키워드 인수는 `.fill_between` 으로 전달됩니다.

    반환값
    -------
    ret : PolyCollection
        Axes 에 추가된 아티스트 (Artist)
    """
    if orientation not in 'hv':
        raise ValueError(f"orientation must be in {{'h', 'v'}} not {orientation}")

    kwargs.setdefault('step', 'post')
    kwargs.setdefault('alpha', 0.7)
    edges = np.asarray(edges)
    values = np.asarray(values)
    if len(edges) - 1 != len(values):
        raise ValueError(f'Must provide one more bin edge than value not: {len(edges)=} {len(values)=}')

    if bottoms is None:
        bottoms = 0
    bottoms = np.broadcast_to(bottoms, values.shape)

    values = np.append(values, values[-1])
    bottoms = np.append(bottoms, bottoms[-1])
    if orientation == 'h':
        return ax.fill_betweenx(edges, values, bottoms, **kwargs)
    elif orientation == 'v':
        return ax.fill_between(edges, values, bottoms, **kwargs)
    else:
        raise AssertionError("you should never be here")
```

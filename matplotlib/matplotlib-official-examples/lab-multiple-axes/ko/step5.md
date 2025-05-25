# 연결선 그리기

다섯 번째 단계는 두 subplot 을 연결하는 점선 (dotted line) 을 그리는 것입니다. 왼쪽 subplot 의 원점을 오른쪽 subplot 의 오른쪽 가장자리 (right edge) 에 연결하는 `ConnectionPatch` 객체를 생성합니다. 또한 애니메이션에서 나중에 업데이트할 `con` 패치 객체를 저장합니다.

```python
con = ConnectionPatch(
    (1, 0),
    (0, 0),
    "data",
    "data",
    axesA=axl,
    axesB=axr,
    color="C0",
    ls="dotted",
)
fig.add_artist(con)
```

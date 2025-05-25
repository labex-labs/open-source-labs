# 두 모델의 부분 의존성 곡선 함께 플롯하기

이 단계에서는 두 모델의 부분 의존성 곡선을 같은 플롯에 그립니다.

```python
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
tree_disp.plot(ax=ax1)
ax1.set_title("의사 결정 트리")
mlp_disp.plot(ax=ax2, line_kw={"color": "red"})
ax2.set_title("다층 퍼셉트론")
```

곡선을 서로 위에 그려 비교하는 또 다른 방법이 있습니다. 여기서 한 행과 두 열을 가진 그림을 만듭니다. 축은 `PartialDependenceDisplay.plot` 함수에 리스트로 전달되어 각 모델의 부분 의존성 곡선을 같은 축에 그립니다. 축 리스트의 길이는 그려지는 플롯의 개수와 같아야 합니다.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 6))
tree_disp.plot(ax=[ax1, ax2], line_kw={"label": "의사 결정 트리"})
mlp_disp.plot(
    ax=[ax1, ax2], line_kw={"label": "다층 퍼셉트론", "color": "red"}
)
ax1.legend()
ax2.legend()
```

`tree_disp.axes_`는 부분 의존성 플롯을 그리기 위해 사용된 축을 저장하는 넘파이 배열 컨테이너입니다. 이를 `mlp_disp`에 전달하여 플롯을 서로 위에 그리는 것과 같은 효과를 얻을 수 있습니다. 또한 `mlp_disp.figure_`는 그림을 저장하여 `plot` 호출 후 그림 크기를 조정할 수 있습니다. 이 경우 `tree_disp.axes_`가 두 차원이므로 `plot`은 왼쪽 가장자리 플롯에만 y 레이블과 y 눈금을 표시합니다.

```python
tree_disp.plot(line_kw={"label": "의사 결정 트리"})
mlp_disp.plot(
    line_kw={"label": "다층 퍼셉트론", "color": "red"}, ax=tree_disp.axes_
)
tree_disp.figure_.set_size_inches(10, 6)
tree_disp.axes_[0, 0].legend()
tree_disp.axes_[0, 1].legend()
plt.show()
```

# 플롯 사용자 정의

플롯을 사용자 정의하기 위해 다음 메서드를 사용할 수 있습니다.

- `set_rmax`를 사용하여 `r`의 최대값을 설정합니다.
- `set_rticks`를 사용하여 `r`의 눈금 값을 설정합니다.
- `set_rlabel_position`을 사용하여 방사형 레이블의 위치를 설정합니다.

```python
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.set_rlabel_position(-22.5)
```

`set_title` 메서드를 사용하여 플롯에 제목을 추가할 수도 있습니다.

```python
ax.set_title("A line plot on a polar axis", va='bottom')
```

마지막으로, `grid` 메서드를 사용하여 플롯에 그리드를 추가할 수 있습니다.

```python
ax.grid(True)
```

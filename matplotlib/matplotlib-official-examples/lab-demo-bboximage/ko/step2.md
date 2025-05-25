# 텍스트를 사용하여 BboxImage 생성

텍스트를 사용하여 BboxImage 를 생성하는 것으로 시작합니다. `text()` 메서드를 사용하여 `text` 객체를 생성하고 이를 `ax1` 객체에 추가합니다. 그런 다음 `add_artist()` 메서드를 사용하여 `BboxImage` 객체를 생성합니다. 텍스트의 경계 상자를 얻기 위해 `text` 객체의 `get_window_extent` 메서드를 `BboxImage` 생성자에 전달합니다. 또한 이미지를 생성하기 위해 (1, 256) 모양의 1 차원 배열을 `BboxImage` 생성자의 `data` 매개변수에 전달합니다.

```python
fig, (ax1, ax2) = plt.subplots(ncols=2)

txt = ax1.text(0.5, 0.5, "test", size=30, ha="center", color="w")
ax1.add_artist(
    BboxImage(txt.get_window_extent, data=np.arange(256).reshape((1, -1))))
```

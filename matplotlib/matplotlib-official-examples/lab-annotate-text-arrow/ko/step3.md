# 방향을 나타내는 텍스트 화살표 추가

데이터의 방향을 나타내기 위해, `ax.text()` 함수와 `boxstyle`을 "rarrow"로 설정한 `bbox` 매개변수를 사용하여 텍스트 화살표를 추가합니다.

```python
bbox_props = dict(boxstyle="rarrow", fc=(0.8, 0.9, 0.9), ec="b", lw=2)
t = ax.text(0, 0, "Direction", ha="center", va="center", rotation=45,
            size=15,
            bbox=bbox_props)

bb = t.get_bbox_patch()
bb.set_boxstyle("rarrow", pad=0.6)
```

# 영역 음영 처리

`fill_between`을 사용하여 사인파가 양수 및 음수인 영역의 수평선 위와 아래를 각각 음영 처리합니다.

```python
ax.fill_between(t, 1, where=s > 0, facecolor='green', alpha=.5)
ax.fill_between(t, -1, where=s < 0, facecolor='red', alpha=.5)
```

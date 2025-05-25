# 사용자 정의 박스 스타일 사용하기

사용자 정의 박스 스타일을 구현하고 등록한 후에는 `Axes.text`와 함께 사용할 수 있습니다.

```python
fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle="angled,pad=0.5", alpha=0.2))
```

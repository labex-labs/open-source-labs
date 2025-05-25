# Y=0 에서 X 축 선 표시

이제 y=0 에서 x 축 선을 표시합니다. 이는 xzero 축을 visible 로 설정하여 수행됩니다.

```python
ax.axis["xzero"].set_visible(True)
ax.axis["xzero"].label.set_text("Axis Zero")
```

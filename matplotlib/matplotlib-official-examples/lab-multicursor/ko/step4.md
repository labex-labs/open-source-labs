# MultiCursor 추가

마지막으로, 데이터 포인트 위에 마우스를 올리면 세 개의 모든 플롯에 커서를 표시하기 위해 `MultiCursor` 함수를 추가합니다.

```python
multi = MultiCursor(None, (ax1, ax2, ax3), color='r', lw=1)
plt.show()
```

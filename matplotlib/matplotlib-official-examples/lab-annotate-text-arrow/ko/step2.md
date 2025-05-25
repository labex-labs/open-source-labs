# 플롯에 텍스트 주석 추가

다음으로, `ax.text()` 함수를 사용하여 플롯에 텍스트 주석을 추가합니다. "Sample A"와 "Sample B"에 대한 두 개의 주석을 생성합니다.

```python
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
ax.text(-2, -2, "Sample A", ha="center", va="center", size=20,
        bbox=bbox_props)
ax.text(2, 2, "Sample B", ha="center", va="center", size=20,
        bbox=bbox_props)
```

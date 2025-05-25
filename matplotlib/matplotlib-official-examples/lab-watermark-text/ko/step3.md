# 텍스트 워터마크 추가

텍스트 워터마크를 추가하려면 `Figure` 객체의 `text()` 메서드를 사용할 수 있습니다. 위치, 텍스트, 글꼴 크기, 색상 및 투명도와 같은 다른 속성을 제공해야 합니다.

```python
ax.text(0.5, 0.5, 'created with matplotlib', transform=ax.transAxes,
        fontsize=40, color='gray', alpha=0.5,
        ha='center', va='center', rotation=30)
```

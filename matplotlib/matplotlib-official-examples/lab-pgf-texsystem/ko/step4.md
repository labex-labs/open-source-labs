# 플롯에 텍스트 추가

`ax.text()` 함수를 사용하여 플롯에 텍스트를 추가할 수 있습니다. 이 예제에서는 서로 다른 글꼴 패밀리를 사용하여 텍스트를 추가합니다.

```python
ax.text(0.5, 3., "serif", family="serif")
ax.text(0.5, 2., "monospace", family="monospace")
ax.text(2.5, 2., "sans-serif", family="sans-serif")
ax.set_xlabel(r"µ is not $\mu$")
```

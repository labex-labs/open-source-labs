# 플롯에 텍스트 추가

`ax.text()` 함수를 사용하여 플롯에 텍스트를 추가합니다. 플롯의 네 가지 다른 위치에 텍스트를 추가하고, 각 텍스트는 서로 다른 글꼴 패밀리 (serif, monospace, sans-serif, cursive) 를 사용합니다.

```python
ax.text(0.5, 3., "serif")
ax.text(0.5, 2., "monospace", family="monospace")
ax.text(2.5, 2., "sans-serif", family="DejaVu Sans")
ax.text(2.5, 1., "comic", family="cursive")
```

# Family 옵션

첫 번째로 살펴볼 글꼴 속성은 family 옵션입니다. 이 속성을 사용하면 플롯에 사용되는 글꼴 패밀리 (family) 를 설정할 수 있습니다.

```python
# Show family options
fig.text(0.1, 0.9, 'family', fontproperties=heading_font, **alignment)
families = ['serif', 'sans-serif', 'cursive', 'fantasy', 'monospace']
for k, family in enumerate(families):
    font = FontProperties()
    font.set_family(family)
    fig.text(0.1, yp[k], family, fontproperties=font, **alignment)
```

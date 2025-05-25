# Size 옵션

다섯 번째로 살펴볼 글꼴 속성은 size 옵션입니다. 이 속성을 사용하면 플롯에 사용되는 글꼴 크기 (size) 를 설정할 수 있습니다.

```python
# Show size options
sizes = [
    'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large']
fig.text(0.9, 0.9, 'size', fontproperties=heading_font, **alignment)
for k, size in enumerate(sizes):
    font = FontProperties()
    font.set_size(size)
    fig.text(0.9, yp[k], size, fontproperties=font, **alignment)
```

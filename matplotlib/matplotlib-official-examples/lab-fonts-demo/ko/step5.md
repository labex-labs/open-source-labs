# Weight 옵션

네 번째로 살펴볼 글꼴 속성은 weight 옵션입니다. 이 속성을 사용하면 플롯에 사용되는 글꼴 굵기 (weight) 를 설정할 수 있습니다.

```python
# Show weight options
weights = ['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black']
fig.text(0.7, 0.9, 'weight', fontproperties=heading_font, **alignment)
for k, weight in enumerate(weights):
    font = FontProperties()
    font.set_weight(weight)
    fig.text(0.7, yp[k], weight, fontproperties=font, **alignment)
```

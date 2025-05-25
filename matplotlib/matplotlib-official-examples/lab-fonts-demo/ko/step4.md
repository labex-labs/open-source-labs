# Variant 옵션

세 번째로 살펴볼 글꼴 속성은 variant 옵션입니다. 이 속성을 사용하면 플롯에 사용되는 글꼴 변형 (variant) 을 설정할 수 있습니다.

```python
# Show variant options
variants = ['normal', 'small-caps']
fig.text(0.5, 0.9, 'variant', fontproperties=heading_font, **alignment)
for k, variant in enumerate(variants):
    font = FontProperties()
    font.set_family('serif')
    font.set_variant(variant)
    fig.text(0.5, yp[k], variant, fontproperties=font, **alignment)
```

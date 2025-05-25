# 글꼴 변형 (font variant) 표시

다음으로, Matplotlib 에서 사용 가능한 다양한 글꼴 변형을 표시합니다. `fig.text()` 메서드를 사용하여 각 글꼴 변형을 표시하며, 변형 이름을 텍스트로, 해당 글꼴 변형을 키워드 인수로 사용합니다.

```python
fig.text(0.5, 0.9, 'variant', **alignment)
variants = ['normal', 'small-caps']
for k, variant in enumerate(variants):
    fig.text(0.5, yp[k], variant, family='serif', variant=variant, **alignment)
```

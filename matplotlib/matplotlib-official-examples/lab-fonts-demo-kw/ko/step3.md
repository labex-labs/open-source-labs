# 글꼴 스타일 (font style) 표시

이제 Matplotlib 에서 사용 가능한 다양한 글꼴 스타일을 표시합니다. `fig.text()` 메서드를 사용하여 각 글꼴 스타일을 표시하며, 스타일 이름을 텍스트로, 해당 글꼴 스타일을 키워드 인수로 사용합니다.

```python
fig.text(0.3, 0.9, 'style', **alignment)
styles = ['normal', 'italic', 'oblique']
for k, style in enumerate(styles):
    fig.text(0.3, yp[k], style, family='sans-serif', style=style, **alignment)
```

# 글꼴 패밀리 (font family) 표시

다음으로, Matplotlib 에서 사용 가능한 다양한 글꼴 패밀리를 표시합니다. `fig.text()` 메서드를 사용하여 각 글꼴 패밀리를 표시하며, 글꼴 패밀리 이름을 텍스트로, 해당 글꼴 패밀리를 키워드 인수로 사용합니다.

```python
alignment = {'horizontalalignment': 'center', 'verticalalignment': 'baseline'}
yp = [0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2]

fig.text(0.1, 0.9, 'family', size='large', **alignment)
families = ['serif', 'sans-serif', 'cursive', 'fantasy', 'monospace']
for k, family in enumerate(families):
    fig.text(0.1, yp[k], family, family=family, **alignment)
```

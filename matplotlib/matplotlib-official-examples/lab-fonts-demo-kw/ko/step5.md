# 글꼴 굵기 (font weight) 표시

이제 Matplotlib 에서 사용 가능한 다양한 글꼴 굵기를 표시합니다. `fig.text()` 메서드를 사용하여 각 글꼴 굵기를 표시하며, 굵기 이름을 텍스트로, 해당 글꼴 굵기를 키워드 인수로 사용합니다.

```python
fig.text(0.7, 0.9, 'weight', **alignment)
weights = ['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black']
for k, weight in enumerate(weights):
    fig.text(0.7, yp[k], weight, weight=weight, **alignment)
```

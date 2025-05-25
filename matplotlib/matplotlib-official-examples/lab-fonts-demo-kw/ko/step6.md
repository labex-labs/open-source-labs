# 글꼴 크기 (font size) 표시

마지막으로, Matplotlib 에서 사용 가능한 다양한 글꼴 크기를 표시합니다. `fig.text()` 메서드를 사용하여 각 글꼴 크기를 표시하며, 크기 이름을 텍스트로, 해당 글꼴 크기를 키워드 인수로 사용합니다.

```python
fig.text(0.9, 0.9, 'size', **alignment)
sizes = [
    'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large']
for k, size in enumerate(sizes):
    fig.text(0.9, yp[k], size, size=size, **alignment)
```

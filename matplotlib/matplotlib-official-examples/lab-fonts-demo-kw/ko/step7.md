# 굵은 기울임꼴 (bold italic) 표시

보너스로, 굵은 글꼴과 기울임꼴 스타일을 모두 사용하여 텍스트를 표시할 수도 있습니다. `fig.text()` 메서드를 사용하여 적절한 스타일, 굵기 및 크기로 텍스트를 표시합니다.

```python
fig.text(0.3, 0.1, 'bold italic',
         style='italic', weight='bold', size='x-small', **alignment)
fig.text(0.3, 0.2, 'bold italic',
         style='italic', weight='bold', size='medium', **alignment)
fig.text(0.3, 0.3, 'bold italic',
         style='italic', weight='bold', size='x-large', **alignment)
```

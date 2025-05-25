# Bold Italic

마지막으로 살펴볼 글꼴 속성은 style 과 weight 옵션의 조합입니다. 이 속성을 사용하면 플롯에 사용되는 글꼴 스타일과 굵기를 설정할 수 있습니다.

```python
# Show bold italic
font = FontProperties(style='italic', weight='bold', size='x-small')
fig.text(0.3, 0.1, 'bold italic', fontproperties=font, **alignment)
font = FontProperties(style='italic', weight='bold', size='medium')
fig.text(0.3, 0.2, 'bold italic', fontproperties=font, **alignment)
font = FontProperties(style='italic', weight='bold', size='x-large')
fig.text(0.3, 0.3, 'bold italic', fontproperties=font, **alignment)
```

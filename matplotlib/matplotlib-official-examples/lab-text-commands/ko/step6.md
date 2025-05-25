# 플롯에 텍스트 추가

`ax.text()` 함수를 사용하여 플롯에 텍스트를 추가할 수 있습니다. 이 함수는 세 개의 인수를 받습니다: x 좌표, y 좌표, 그리고 텍스트 문자열입니다. `style`, `bbox`, 그리고 `fontsize` 인수를 사용하여 텍스트 스타일을 사용자 정의할 수 있습니다.

```python
ax.text(3, 8, 'boxed italics text in data coords', style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

ax.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)

ax.text(3, 2, 'Unicode: Institut f\374r Festk\366rperphysik')

ax.text(0.95, 0.01, 'colored text in axes coords',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=15)
```

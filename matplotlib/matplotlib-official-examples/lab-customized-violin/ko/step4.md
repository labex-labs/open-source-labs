# 축 스타일 설정

마지막으로, 눈금 레이블과 제한을 지정하여 x 축의 스타일을 설정합니다. 이를 수행하기 위해 헬퍼 함수 `set_axis_style`을 정의합니다.

```python
# set style for the axes
labels = ['A', 'B', 'C', 'D']
set_axis_style(ax2, labels)

def set_axis_style(ax, labels):
    ax.set_xticks(np.arange(1, len(labels) + 1))
    ax.set_xticklabels(labels)
    ax.set_xlim(0.25, len(labels) + 0.75)
    ax.set_xlabel('Sample Name')
```

# 패치 및 툴팁 주석 추가

그런 다음 패치와 툴팁 주석을 플롯에 추가합니다. 툴팁 주석은 `annotate` 메서드를 사용하여 생성됩니다. `xy` 매개변수를 패치의 좌표로 설정하고, `xytext`를 `(0, 0)`으로 설정하여 툴팁을 패치 바로 위에 배치합니다. 또한 `textcoords` 매개변수를 `'offset points'`로 설정하여 툴팁을 패치에 정렬합니다. `color` 매개변수를 `'w'`로 설정하여 텍스트를 흰색으로 만들고, `ha`를 `'center'`로 설정하여 텍스트를 가로로 가운데 정렬하며, `fontsize`를 `8`로 설정하여 글꼴 크기를 설정하고, `bbox`를 사용하여 툴팁 상자의 스타일을 설정합니다.

```python
for i, (item, label) in enumerate(zip(shapes, labels)):
    patch = ax.add_patch(item)
    annotate = ax.annotate(labels[i], xy=item.get_xy(), xytext=(0, 0),
                           textcoords='offset points', color='w', ha='center',
                           fontsize=8, bbox=dict(boxstyle='round, pad=.5',
                                                 fc=(.1, .1, .1, .92),
                                                 ec=(1., 1., 1.), lw=1,
                                                 zorder=1))

    ax.add_patch(patch)
    patch.set_gid(f'mypatch_{i:03d}')
    annotate.set_gid(f'mytooltip_{i:03d}')
```

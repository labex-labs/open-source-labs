# 그림 생성 및 대체 커서 설정

다음으로, 그림을 생성하고 루프를 사용하여 각 서브플롯에 대한 대체 커서를 설정합니다. 또한 사용 중인 커서를 나타내기 위해 각 서브플롯에 텍스트를 추가합니다.

```python
fig, axs = plt.subplots(len(Cursors), figsize=(6, len(Cursors) + 0.5), gridspec_kw={'hspace': 0})
fig.suptitle('Hover over an Axes to see alternate Cursors')

for cursor, ax in zip(Cursors, axs):
    ax.cursor_to_use = cursor
    ax.text(0.5, 0.5, cursor.name,
            horizontalalignment='center', verticalalignment='center')
    ax.set(xticks=[], yticks=[])
```

# Sankey 다이어그램 사용자 정의

흐름 (flows), 레이블 (labels), 방향 (orientations) 및 기타 매개변수를 변경하여 Sankey 다이어그램을 사용자 정의할 수 있습니다. 이 예제에서는 더 긴 경로와 중간에 레이블이 있는 다이어그램을 만들 것입니다.

```python
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[],
                     title="Flow Diagram of a Widget")
sankey = Sankey(ax=ax, scale=0.01, offset=0.2, head_angle=180,
                format='%.0f', unit='%')
sankey.add(flows=[25, 0, 60, -10, -20, -5, -15, -10, -40],
           labels=['', '', '', 'First', 'Second', 'Third', 'Fourth',
                   'Fifth', 'Hurray!'],
           orientations=[-1, 1, 0, 1, 1, 1, -1, -1, 0],
           pathlengths=[0.25, 0.25, 0.25, 0.25, 0.25, 0.6, 0.25, 0.25,
                        0.25],
           patchlabel="Widget\nA")  # Arguments to matplotlib.patches.PathPatch
diagrams = sankey.finish()
diagrams[0].texts[-1].set_color('r')
diagrams[0].text.set_fontweight('bold')
```

이 코드는 더 긴 경로, 중간에 레이블, 그리고 기타 사용자 정의된 매개변수를 가진 Sankey 다이어그램을 생성합니다. 결과 다이어그램은 "Flow Diagram of a Widget"라는 제목으로 표시됩니다.

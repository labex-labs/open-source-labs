# Sankey 다이어그램에서 두 시스템 연결하기

Sankey 다이어그램에서 두 시스템을 연결할 수도 있습니다. 이 예제에서는 연결된 두 시스템이 있는 다이어그램을 만들 것입니다.

```python
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[], title="Two Systems")
flows = [0.25, 0.15, 0.60, -0.10, -0.05, -0.25, -0.15, -0.10, -0.35]
sankey = Sankey(ax=ax, unit=None)
sankey.add(flows=flows, label='one',
           orientations=[-1, 1, 0, 1, 1, 1, -1, -1, 0])
sankey.add(flows=[-0.25, 0.15, 0.1], label='two',
           orientations=[-1, -1, -1], prior=0, connect=(0, 0))
diagrams = sankey.finish()
diagrams[-1].patch.set_hatch('/')
plt.legend()
```

이 코드는 연결된 두 시스템이 있는 Sankey 다이어그램을 생성합니다. 결과 다이어그램은 "Two Systems"라는 제목으로 표시됩니다.

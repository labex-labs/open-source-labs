# 간단한 Sankey 다이어그램 만들기

Sankey 클래스를 사용하는 방법을 보여주는 간단한 Sankey 다이어그램을 만드는 것으로 시작합니다.

```python
Sankey(flows=[0.25, 0.15, 0.60, -0.20, -0.15, -0.05, -0.50, -0.10],
       labels=['', '', '', 'First', 'Second', 'Third', 'Fourth', 'Fifth'],
       orientations=[-1, 1, 0, 1, 1, 1, 0, -1]).finish()
plt.title("The default settings produce a diagram like this.")
```

이 코드는 기본 설정을 사용하여 Sankey 다이어그램을 생성합니다. 여기에는 흐름의 레이블과 방향이 포함됩니다. 결과 다이어그램은 "The default settings produce a diagram like this."라는 제목으로 표시됩니다.

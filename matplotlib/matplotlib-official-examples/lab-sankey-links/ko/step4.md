# `corner` 함수 정의

다음으로, 코너 링크를 생성하는 `corner` 함수를 정의합니다.

```python
def corner(sankey):
    """Generate a corner link."""
    prior = len(sankey.diagrams)
    sankey.add(flows=[1, -1], orientations=[0, 1],
               patchlabel=str(prior), facecolor='k',
               prior=prior - 1, connect=(1, 0), alpha=0.5)
```

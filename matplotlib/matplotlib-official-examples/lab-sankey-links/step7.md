# Add the first diagram

We add the first diagram using `sankey.add()` with `flows=[1, -1]` and `orientations=[0, 1]`.

```python
sankey.add(flows=[1, -1], orientations=[0, 1],
           patchlabel="0", facecolor='k',
           rotation=45)
```

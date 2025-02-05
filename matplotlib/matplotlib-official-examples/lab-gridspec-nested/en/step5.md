# Create Another Inner GridSpec

We will now create another inner gridspec. This time, we will use the `subgridspec` method to create a 3 by 3 gridspec that will be a subplot of the second column of the outer gridspec.

```python
gs01 = gs0[1].subgridspec(3, 3)
```

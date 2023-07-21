# Create the Inner GridSpec

Now, we will create the inner gridspec. We will use the `GridSpecFromSubplotSpec` method to create a 3 by 3 gridspec that will be a subplot of the outer gridspec.

```python
gs00 = gridspec.GridSpecFromSubplotSpec(3, 3, subplot_spec=gs0[0])
```

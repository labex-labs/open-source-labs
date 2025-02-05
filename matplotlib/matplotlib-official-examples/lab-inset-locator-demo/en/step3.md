# Turn Off Tick Labels

To remove the tick labels from each of the insets, we can use the `tick_params()` method and set `labelleft` and `labelbottom` to `False`.

```python
# Turn ticklabels of insets off
for axi in [axins, axins2, axins3, axins4]:
    axi.tick_params(labelleft=False, labelbottom=False)
```

# Set the recurrence rule

You will be setting custom date ticks on every 5th Easter. To do this, you need to set the recurrence rule using the rrulewrapper function.

```python
rule = rrulewrapper(YEARLY, byeaster=1, interval=5)
```

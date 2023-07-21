# Perform Exponentially Weighted Window Operation

Perform an exponentially weighted window operation and then calculate the mean for each window.

```python
# Perform an exponentially weighted window operation and calculate the mean for each window
s.ewm(span=3).mean()
```

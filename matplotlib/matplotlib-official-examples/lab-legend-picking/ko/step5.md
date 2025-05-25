# 범례 선을 원래 선에 매핑

사전을 사용하여 범례 선을 원래 선에 매핑합니다.

```python
lines = [line1, line2]
lined = {}  # Will map legend lines to original lines.
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(True)  # Enable picking on the legend line.
    lined[legline] = origline
```

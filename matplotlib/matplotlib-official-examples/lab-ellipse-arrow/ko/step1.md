# Matplotlib 가져오기 및 Figure 와 Axis 생성

먼저, Matplotlib 을 가져오고 figure 와 axis 를 생성해야 합니다. Figure 와 axis 는 플롯을 위한 컨테이너입니다.

```python
import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots(subplot_kw={"aspect": "equal"})
```

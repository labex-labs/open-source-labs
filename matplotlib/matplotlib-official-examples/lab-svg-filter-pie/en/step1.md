# Create a Pie Chart

We will create a square figure and axes for our pie chart. We will define the labels and fracs for the chart. We will also set the explode values for the chart slices. Finally, we will draw the pie chart with the defined parameters.

```python
import matplotlib.pyplot as plt
from matplotlib.patches import Shadow

fig = plt.figure(figsize=(6, 6))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
fracs = [15, 30, 45, 10]
explode = (0, 0.05, 0, 0)

pies = ax.pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%')

for w in pies[0]:
    w.set_gid(w.get_label())
    w.set_edgecolor("none")

for w in pies[0]:
    s = Shadow(w, -0.01, -0.01)
    s.set_gid(w.get_gid() + "_shadow")
    s.set_zorder(w.get_zorder() - 0.1)
    ax.add_patch(s)

plt.show()
```

# Create the Bar Chart

The next step is to create the bar chart. We will use the `bar()` function to create the chart. We will create two sets of bars, one for tea and one for coffee. We will also add error bars to the chart.

```python
ax.bar(ind, tea_means, width, bottom=0*cm, yerr=tea_std, label='Tea')
ax.bar(ind + width, coffee_means, width, bottom=0*cm, yerr=coffee_std,
       label='Coffee')
```

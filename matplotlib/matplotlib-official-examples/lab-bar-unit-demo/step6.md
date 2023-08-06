# Add Labels and Title to the Chart

The final step is to add labels and a title to the chart. We will add a title to the chart, a label for the x-axis, and a legend for the chart.

```python
ax.set_title('Cup height by group and beverage choice')
ax.set_xlabel('Group')
ax.legend()
ax.autoscale_view()
```

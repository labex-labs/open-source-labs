# Create a simple Sankey diagram

We will start by creating a simple Sankey diagram that demonstrates how to use the Sankey class.

```python
Sankey(flows=[0.25, 0.15, 0.60, -0.20, -0.15, -0.05, -0.50, -0.10],
       labels=['', '', '', 'First', 'Second', 'Third', 'Fourth', 'Fifth'],
       orientations=[-1, 1, 0, 1, 1, 1, 0, -1]).finish()
plt.title("The default settings produce a diagram like this.")
```

This code will produce a Sankey diagram with default settings, which includes the labels and orientations of the flows. The resulting diagram will be displayed with the title "The default settings produce a diagram like this."

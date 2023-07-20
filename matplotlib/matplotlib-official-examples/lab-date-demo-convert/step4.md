# Create the graph

Now, we can create the graph using the dates and y values. We will first create a figure and axis object using the subplots function. Then, we will plot the graph using the plot function. Copy and paste the following code:

```python
fig, ax = plt.subplots()
ax.plot(dates, y**2, 'o')
```

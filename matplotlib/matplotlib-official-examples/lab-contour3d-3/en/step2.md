# Create 3D figure and data

In this step, we will create a 3D figure and get test data for the surface plot.

```python
# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Get test data for the surface plot
X, Y, Z = axes3d.get_test_data(0.05)
```

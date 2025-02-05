# Define the Direction of the Arrows

Now we will define the direction of the arrows. In this example, we will define the direction of the arrows using NumPy's trigonometric functions. The `sin` and `cos` functions are used to create the `u`, `v`, and `w` arrays that represent the direction of the arrows in the `x`, `y`, and `z` directions.

```python
u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
     np.sin(np.pi * z))
```

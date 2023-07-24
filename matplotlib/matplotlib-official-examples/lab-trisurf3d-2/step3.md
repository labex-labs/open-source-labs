# Define the Surface

Next, we define the surface. In this example, we use a Mobius mapping to take a `u`, `v` pair and return an `x`, `y`, `z` triple.

```python
x = (1 + 0.5 * v * np.cos(u / 2.0)) * np.cos(u)
y = (1 + 0.5 * v * np.cos(u / 2.0)) * np.sin(u)
z = 0.5 * v * np.sin(u / 2.0)
```

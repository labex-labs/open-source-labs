# Create the Mesh

Next, we will create the mesh in polar coordinates and compute corresponding Z. We will create an array of radius values `r`, an array of angle values `p`, and then use NumPy's `meshgrid()` function to create a grid of `R` and `P` values. Finally, we will use the `Z` equation to compute the height of each point on the surface.

```python
r = np.linspace(0, 1.25, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r, p)
Z = ((R**2 - 1)**2)
```

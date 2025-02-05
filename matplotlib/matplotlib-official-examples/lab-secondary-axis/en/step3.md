# Create the Secondary Axis

We will now create the secondary axis and convert the x-axis from degrees to radians. We will use `deg2rad` as the forward function and `rad2deg` as the inverse function.

```python
def deg2rad(x):
    return x * np.pi / 180

def rad2deg(x):
    return x * 180 / np.pi

secax = ax.secondary_xaxis('top', functions=(deg2rad, rad2deg))
secax.set_xlabel('angle [rad]')
```

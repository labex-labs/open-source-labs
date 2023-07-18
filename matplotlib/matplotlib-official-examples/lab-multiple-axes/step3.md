# Draw the Circle and Initial Point

The third step is to draw the circle and initial point on the left subplot. We create an array of angles to generate the circle, and then plot the sine and cosine of each angle. We also plot a single point at the origin.

```python
x = np.linspace(0, 2 * np.pi, 50)
axl.plot(np.cos(x), np.sin(x), "k", lw=0.3)
point, = axl.plot(0, 0, "o")
```

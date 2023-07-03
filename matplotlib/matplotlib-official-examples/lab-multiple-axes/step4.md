# Draw the Sine Curve

The fourth step is to draw the sine curve on the right subplot. We create an array of angles, and then plot the sine of each angle. We also save the `sine` plot object, which we will update later in the animation.

```python
sine, = axr.plot(x, np.sin(x))
```

#

# Draw the Connection Line

The fifth step is to draw a dotted line connecting the two subplots. We create a `ConnectionPatch` object that connects the origin of the left subplot to the right edge of the right subplot. We also save the `con` patch object, which we will update later in the animation.

```python
con = ConnectionPatch(
    (1, 0),
    (0, 0),
    "data",
    "data",
    axesA=axl,
    axesB=axr,
    color="C0",
    ls="dotted",
)
fig.add_artist(con)
```

#

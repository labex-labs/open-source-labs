# Create an Anchored Offset Box

Create an anchored offset box using AnnotationBbox to add the offset box and set its position. Use the following code to create the anchored offset box:

```python
ao = AnchoredOffsetbox(loc='upper left', child=offsetbox, frameon=True,
                           borderpad=0.2)
ax1.add_artist(ao)
```

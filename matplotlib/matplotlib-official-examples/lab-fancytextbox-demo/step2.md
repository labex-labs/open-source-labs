# Create a Text Box

```python
plt.text(0.6, 0.7, "eggs", size=50, rotation=30.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
```

We create a text box containing the word "eggs" using the `text()` method. The `bbox` parameter is used to style the box. The `boxstyle` parameter is set to "round" to create a rounded box, while `ec` and `fc` parameters set the edge and face colors of the box, respectively. The `size` parameter sets the font size, `rotation` parameter sets the rotation angle, and `ha` and `va` parameters set the horizontal and vertical alignment of the text in the box.

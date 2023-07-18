# Create Another Text Box

```python
plt.text(0.55, 0.6, "spam", size=50, rotation=-25.,
         ha="right", va="top",
         bbox=dict(boxstyle="square",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
```

We create another text box containing the word "spam". This time we set `boxstyle` parameter to "square" to create a square box and set `ha` and `va` parameters to "right" and "top" to align the text to the right and top of the box.

# Draw texts to a figure with positioning in pixel coordinates

Alternatively, we can directly draw text to a figure with positioning in pixel coordinates by using `.Figure.text` together with `.transforms.IdentityTransform`.

```python
fig.text(100, 250, r"IQ: $\sigma_i=15$", color="blue", fontsize=20, transform=IdentityTransform())
fig.text(100, 350, r"some other string", color="red", fontsize=20, transform=IdentityTransform())

plt.show()
```

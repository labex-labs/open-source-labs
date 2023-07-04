# Save the plot

Finally, we can save our plot to disk. Follow these steps:

1. Print the supported file formats using `print(fig.canvas.get_supported_filetypes())`.

```python
print(fig.canvas.get_supported_filetypes())
```

2. Save the figure as an image file using `fig.savefig(file_path, transparent=False, dpi=80, bbox_inches="tight")`. Uncomment this line to save the figure.

```python
fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches="tight")
```

# Add Text Watermark

To add a text watermark, we can use the `text()` method of the `Figure` object. We need to provide the position, text, and other properties like font size, color, and transparency.

```python
ax.text(0.5, 0.5, 'created with matplotlib', transform=ax.transAxes,
        fontsize=40, color='gray', alpha=0.5,
        ha='center', va='center', rotation=30)
```

#

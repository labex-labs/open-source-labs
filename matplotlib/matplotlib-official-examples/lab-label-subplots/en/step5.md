# Label with Title

If we want the label to be aligned with the title, we can incorporate it into the title or use the `loc` keyword argument.

```python
for label, ax in axs.items():
    ax.set_title('Normal Title', fontstyle='italic')
    ax.set_title(label, fontfamily='serif', loc='left', fontsize='medium')
```

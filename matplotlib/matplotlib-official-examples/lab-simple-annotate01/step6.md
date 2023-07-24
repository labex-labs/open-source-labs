# Customize Annotations

We can customize the annotations by changing the font size, font color, and arrow style. The following code will change the font size, font color, and arrow style of the text annotation.

```python
ax.annotate("Data Point 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05, arrowstyle="->"),
            fontsize=12, color="red")
```

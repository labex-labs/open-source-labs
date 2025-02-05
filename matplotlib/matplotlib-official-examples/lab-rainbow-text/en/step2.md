# Create the Subsequent Text Objects

The next step is to create the subsequent text objects using `~.Axes.annotate`. This function allows you to position the text object relative to the previous text object. The following code creates three text objects that are positioned to the right of the previous text object.

```python
text = ax.annotate(
    " says,", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="gold", weight="bold")  # custom properties
text = ax.annotate(
    " hello", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="green", style="italic")  # custom properties
text = ax.annotate(
    " world!", xycoords=text, xy=(1, 0), verticalalignment="bottom",
    color="blue", family="serif")  # custom properties
```

# Wrapping Text Automatically

Now, let's explore how to wrap text automatically in Matplotlib. Replace the `plt.text()` line in your code with the following:

```python
t = ("This is a really long string that I'd rather have wrapped so that it "
     "doesn't go outside of the figure, but if it's long enough it will go "
     "off the top or bottom!")
plt.text(5, 5, t, ha='center', wrap=True)
```

The `wrap=True` argument tells Matplotlib to wrap the text automatically.

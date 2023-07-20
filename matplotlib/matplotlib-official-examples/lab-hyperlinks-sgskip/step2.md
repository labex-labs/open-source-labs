# Create a Scatter Plot with Hyperlinks

In this step, we will create a scatter plot and add hyperlinks to the markers. Here's the code to create the scatter plot:

```python
fig = plt.figure()
s = plt.scatter([1, 2, 3], [4, 5, 6])
```

To add hyperlinks, we need to use the `set_urls()` method of the scatter plot object. This method takes a list of URLs as its argument. Here's the updated code:

```python
s.set_urls(['https://www.bbc.com/news', 'https://www.google.com/', None])
```

The first two markers will have hyperlinks to `https://www.bbc.com/news` and `https://www.google.com/`, respectively. The third marker will not have a hyperlink. Finally, we can save the plot as an SVG file using `fig.savefig()`:

```python
fig.savefig('scatter.svg')
```

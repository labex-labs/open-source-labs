# Adding Text to the Plot

We can add text to the plot using the `text` function. We can specify the position, rotation, horizontal and vertical alignment, and multialignment of the text.

```python
ax0.text(2, 7, 'this is\nyet another test',
         rotation=45,
         horizontalalignment='center',
         verticalalignment='top',
         multialignment='center')
```

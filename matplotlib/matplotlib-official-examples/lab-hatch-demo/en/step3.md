# Create a Bar Plot with Hatching

Now that you have your data, you can create a bar plot with hatching. You can use hatching to create patterns on the bars in your plot. In this case, we will be using the hatch parameter to add hatching to our bars.

```python
plt.bar(x, y1, edgecolor='black', hatch="/")
plt.bar(x, y2, bottom=y1, edgecolor='black', hatch='//')
```

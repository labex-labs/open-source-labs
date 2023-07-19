# Save the Plot

You can save the plot as an image file using the `savefig` method. The following code saves the plot as a PNG image:

```python
plt.plot([1, 2, 3, 4], 'o-r')
plt.title('Simple Plot')
plt.xlabel('Index')
plt.ylabel('Numbers')
plt.savefig('simple_plot.png')
```

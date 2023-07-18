# Customize the plot

We can customize the plot by adding labels to the x and y axes, a title to the plot, and a legend. We can also change the line style and color.

```python
plt.plot(x, y, linestyle='--', color='red', label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Plot')
plt.legend()
```

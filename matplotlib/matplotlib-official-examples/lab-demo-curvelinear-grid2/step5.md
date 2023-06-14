# Create the Figure

The final step is to create the figure using the `plt.figure` function. We will set the figure size to (7, 4) and call the `curvelinear_test1` function created in Steps 2-4.

```python
if __name__ == "__main__":
    fig = plt.figure(figsize=(7, 4))
    curvelinear_test1(fig)
    plt.show()
```

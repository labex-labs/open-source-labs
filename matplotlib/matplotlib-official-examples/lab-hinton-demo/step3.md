# Generating a Hinton Diagram

Now, we will generate a random weight matrix using numpy and then use the `hinton` function to generate the Hinton diagram.

```python
if __name__ == '__main__':
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    hinton(np.random.rand(20, 20) - 0.5)
    plt.show()
```

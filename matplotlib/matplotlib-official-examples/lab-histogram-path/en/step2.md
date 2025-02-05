# Set the random seed and generate data

We will use numpy to generate random data. In order to make our results reproducible, we will set a random seed. Add the following code to your file:

```python
np.random.seed(19680801)
data = np.random.randn(1000)
```

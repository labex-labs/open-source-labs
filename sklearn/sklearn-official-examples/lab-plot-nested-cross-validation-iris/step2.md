# Define the Hyperparameters

Next, we define the hyperparameters to be optimized for the support vector classifier. In this case, we optimize the cost parameter `C` and the kernel coefficient `gamma`.

```python
# Set up possible values of parameters to optimize over
p_grid = {"C": [1, 10, 100], "gamma": [0.01, 0.1]}
```



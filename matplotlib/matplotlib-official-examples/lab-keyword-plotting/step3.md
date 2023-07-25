# Create Data

In this step, we will create a dictionary `data` containing values for variables `a`, `b`, `c`, and `d`.

```python
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
```

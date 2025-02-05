# Prepare the Data

The data for the chart is prepared in this step. We will create a list of people's names, their performance, and the error rate.

```python
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))
```

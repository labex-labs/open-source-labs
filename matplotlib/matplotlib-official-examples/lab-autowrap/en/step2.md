# Creating a Basic Plot

Let's start by creating a basic plot with a text element. In your Python script, add the following code:

```python
import matplotlib.pyplot as plt

fig = plt.figure()
plt.axis([0, 10, 0, 10])
plt.text(5, 5, "Hello, Matplotlib!", ha='center')
plt.show()
```

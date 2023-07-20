# Creating the Bar Chart

Now we are ready to create our bar chart. We will start by defining some variables that will help us to set the width of the bars and their position on the x-axis.

```python
dim = len(data[0])
w = 0.75
dimw = w / dim
```

Next, we will create a figure and an axis object using the `subplots()` method. Then, we will use a for loop to iterate through each value in our dataset and create a bar for each one.

```python
fig, ax = plt.subplots()
x = np.arange(len(data))
for i in range(len(data[0])):
    y = [d[i] for d in data]
    b = ax.bar(x + i * dimw, y, dimw, bottom=0.001)
```

We set the `bottom` parameter to `0.001` to avoid having any bars with a height of 0, which is not compatible with a logarithmic scale.

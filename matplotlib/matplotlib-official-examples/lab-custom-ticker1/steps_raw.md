# Custom Ticker Lab

## Introduction

In this lab, you will learn how to create a custom ticker in Python Matplotlib using the `ticker` module. The custom ticker will format the y-axis ticks in millions of dollars.

## Steps

### Step 1: Import Required Libraries

First, we need to import the required libraries to create the custom ticker. We need the `pyplot` and `ticker` modules from Matplotlib.

```python
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
```

### Step 2: Define Custom Ticker Function

Next, we need to define the custom ticker function. The custom ticker function takes two arguments - the value and tick position - and returns the formatted tick label. In this case, we will format the tick label as dollars in millions.

```python
def millions(x, pos):
    """The two arguments are the value and tick position."""
    return f'${x*1e-6:1.1f}M'
```

### Step 3: Create the Plot

Now, we can create the plot with the custom ticker. We will create a bar chart with sample data and set the y-axis ticker to use our custom ticker function.

```python
# Create a bar chart with sample data
fig, ax = plt.subplots()
money = [1.5e5, 2.5e6, 5.5e6, 2.0e7]
ax.bar(['Bill', 'Fred', 'Mary', 'Sue'], money)

# Set the y-axis ticker to use the custom ticker function
ax.yaxis.set_major_formatter(ticker.FuncFormatter(millions))

# Display the plot
plt.show()
```

### Step 4: Interpret the Output

The output of the code should be a bar chart with the y-axis labels formatted in millions of dollars. The tick labels will be formatted as `$0.2M`, `$2.5M`, `$5.5M`, and `$20.0M` respectively.

## Summary

In this lab, you learned how to create a custom ticker in Python Matplotlib using the `ticker` module. You also learned how to format the tick labels in millions of dollars using a custom ticker function. This technique can be useful when working with large financial data sets.

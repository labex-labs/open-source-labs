# Creating a Jupyter Notebook and Preparing the Data

In this first step, we will create a new Jupyter Notebook and set up our data for visualization.

## Creating a New Notebook

1. In the WebIDE interface, locate the "placing-text-boxes.ipynb" file in the file explorer.

2. Click on this file to open it in the Jupyter Notebook interface.

3. In the first cell of the notebook, let's import the necessary libraries. Type the following code and run it by clicking the "Run" button or pressing Shift+Enter:

```python
import matplotlib.pyplot as plt
import numpy as np
```

This code imports two essential libraries:

- `matplotlib.pyplot`: A collection of functions that make matplotlib work like MATLAB
- `numpy`: A fundamental package for scientific computing in Python

## Creating Sample Data

Now, let's create some sample data that we will visualize. In a new cell, enter and run the following code:

```python
# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate 10,000 random numbers from a normal distribution
x = 30 * np.random.randn(10000)

# Calculate basic statistics
mu = x.mean()
median = np.median(x)
sigma = x.std()

# Display the statistics
print(f"Mean (μ): {mu:.2f}")
print(f"Median: {median:.2f}")
print(f"Standard Deviation (σ): {sigma:.2f}")
```

When you run this cell, you should see output similar to:

```
Mean (μ): -0.31
Median: -0.28
Standard Deviation (σ): 29.86
```

The exact values may vary slightly. We've created a dataset with 10,000 random numbers generated from a normal distribution and calculated three important statistics:

1. Mean (μ): The average value of all data points
2. Median: The middle value when data is arranged in order
3. Standard Deviation (σ): A measure of how spread out the data is

These statistics will be used later to annotate our visualization.

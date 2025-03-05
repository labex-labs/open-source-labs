# Preparing the Environment and Creating Data

In this first step, we will set up our working environment by importing the necessary libraries and creating sample data for our visualization. We will focus on generating data that includes some outliers, which will demonstrate the value of using a broken axis plot.

## Import Required Libraries

Let's start by importing the libraries we need for this tutorial. We will use Matplotlib for creating our visualizations and NumPy for generating and manipulating numerical data.

Create a new cell in your Jupyter Notebook and type the following code:

```python
import matplotlib.pyplot as plt
import numpy as np

# Print library versions to confirm they are installed correctly
print(f"Matplotlib version: {plt.__version__}")
print(f"NumPy version: {np.__version__}")
```

When you run this cell, you should see output similar to this:

```
Matplotlib version: 3.5.1
NumPy version: 1.21.5
```

The exact version numbers may vary depending on your environment, but this confirms the libraries are properly installed and ready to use.

## Generate Sample Data with Outliers

Now, let's create a sample dataset that includes some outliers. We'll generate random numbers and then deliberately add larger values to certain positions to create our outliers.

Create a new cell and add the following code:

```python
# Set random seed for reproducibility
np.random.seed(19680801)

# Generate 30 random points with values between 0 and 0.2
pts = np.random.rand(30) * 0.2

# Add 0.8 to two specific points to create outliers
pts[[3, 14]] += 0.8

# Display the first few data points to understand our dataset
print("First 10 data points:")
print(pts[:10])
print("\nData points containing outliers:")
print(pts[[3, 14]])
```

When you run this cell, you should see output similar to:

```
First 10 data points:
[0.01182225 0.11765474 0.07404329 0.91088185 0.10502995 0.11190702
 0.14047499 0.01060192 0.15226977 0.06145634]

Data points containing outliers:
[0.91088185 0.97360754]
```

In this output, you can clearly see that the values at indices 3 and 14 are much larger than the other values. These are our outliers. Most of our data points are below 0.2, but these two outliers are above 0.9, creating a significant disparity in our dataset.

This kind of data distribution is perfect for demonstrating the usefulness of a broken axis plot. In the next step, we will create the plot structure and configure it to properly display both the main data and the outliers.

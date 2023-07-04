# Partial Dependence and Individual Conditional Expectation

## Introduction

Partial dependence plots (PDP) and individual conditional expectation (ICE) plots are useful tools for visualizing and analyzing the interaction between the target response and a set of input features. PDPs show the dependence between the target response and the input features, while ICE plots visualize the dependence of the prediction on a feature for each individual sample. These plots help us understand the relationship between the target response and the input features.

## Steps

### Step 1: Import the necessary libraries

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import plot_partial_dependence, partial_dependence
```

### Step 2: Load and prepare the data

```python
data = load_boston()
X = data.data
y = data.target
feature_names = data.feature_names

# Create a DataFrame for easier data manipulation
df = pd.DataFrame(X, columns=feature_names)
```

### Step 3: Train a Random Forest model

```python
model = RandomForestRegressor()
model.fit(X, y)
```

### Step 4: Create and visualize partial dependence plots

```python
fig, ax = plot_partial_dependence(model, X, features=[(0, 1), (2, 3)], feature_names=feature_names, grid_resolution=20)

# Set figure size and title
fig.set_size_inches(10, 8)
fig.suptitle('Partial Dependence Plots')

plt.show()
```

### Step 5: Create and visualize individual conditional expectation plots

```python
fig, ax = plot_partial_dependence(model, X, features=[(0, 1), (2, 3)], feature_names=feature_names, kind='individual')

# Set figure size and title
fig.set_size_inches(10, 8)
fig.suptitle('Individual Conditional Expectation Plots')

plt.show()
```

### Step 6: Compute partial dependence values for a specific feature

```python
x_index = 0
pdp, axes = partial_dependence(model, X, features=[x_index], grid_resolution=20)

# Plot the partial dependence values
plt.plot(axes[x_index], pdp[0])
plt.xlabel(feature_names[x_index])
plt.ylabel("Partial Dependence")
plt.title("Partial Dependence Plot")

plt.show()
```

### Step 7: Compute individual conditional expectation values for a specific feature

```python
x_index = 0
ice, axes = partial_dependence(model, X, features=[x_index], kind='individual')

# Plot the individual conditional expectation values
for i in range(len(ice)):
    plt.plot(axes[x_index], ice[i], color='lightgray')
plt.plot(axes[x_index], np.mean(ice, axis=0), color='blue')
plt.xlabel(feature_names[x_index])
plt.ylabel("Individual Conditional Expectation")
plt.title("Individual Conditional Expectation Plot")

plt.show()
```

## Summary

Partial dependence plots and individual conditional expectation plots are powerful tools for visualizing and understanding the relationship between the target response and the input features. PDPs provide an overall view of the dependence, while ICE plots show the individual variations. By using these plots, we can gain insights into how the target response changes with respect to different values of the input features.

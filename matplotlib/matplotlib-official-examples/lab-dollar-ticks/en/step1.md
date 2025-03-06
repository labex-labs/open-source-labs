# Setting Up Libraries and Creating Sample Data

In this first step, we will import the necessary libraries and create sample financial data for our plot. We need to import both Matplotlib for visualization and NumPy for data generation.

In the first cell of your notebook, enter and run the following code to import the required libraries:

```python
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Display plots inline in the notebook
%matplotlib inline

print("Libraries imported successfully!")
```

After running the code (press Shift+Enter), you should see the output:

```
Libraries imported successfully!
```

![libraries-imported](../assets/screenshot-20250306-BN9E08ez@2x.png)

Now, let's create some sample financial data to visualize. Financial data often represents values over time, so we'll create a simple dataset that might represent daily revenue over a period of time.

In a new cell, add and run the following code:

```python
# Set a random seed for reproducibility
np.random.seed(42)

# Generate financial data: 30 days of revenue data
days = np.arange(1, 31)
daily_revenue = np.random.uniform(low=1000, high=5000, size=30)

print("Sample of daily revenue data (first 5 days):")
for i in range(5):
    print(f"Day {days[i]}: ${daily_revenue[i]:.2f}")
```

After running this code, you will see the first 5 days of our sample revenue data:

```
Sample of daily revenue data (first 5 days):
Day 1: $3745.40
Day 2: $3992.60
Day 3: $2827.45
Day 4: $4137.54
Day 5: $1579.63
```

This sample data represents daily revenue values between $1,000 and $5,000 for a 30-day period. We'll use this data to create our plot in the next step.

# Import the Required Libraries and Load the Data

Let's start by importing the necessary libraries and loading a dataset. In this example, we will use the Iris dataset.

```python
import numpy as np
from sklearn.model_selection import validation_curve
from sklearn.datasets import load_iris
from sklearn.linear_model import Ridge

np.random.seed(0)
X, y = load_iris(return_X_y=True)
```

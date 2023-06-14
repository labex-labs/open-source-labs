# Import Libraries

We will start by importing the necessary libraries for this lab. We will use the scikit-learn library to generate the dataset and train the logistic regression models, and the matplotlib library to plot the decision boundary.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.inspection import DecisionBoundaryDisplay
```



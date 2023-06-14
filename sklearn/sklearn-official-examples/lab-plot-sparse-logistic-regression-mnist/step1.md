# Import Libraries

We will start by importing the necessary libraries for this lab. We will use scikit-learn library to fetch the dataset, train the model, and evaluate the performance of the model.

```python
import time
import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import check_random_state
```



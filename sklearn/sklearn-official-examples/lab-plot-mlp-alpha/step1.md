# Import Libraries

We will start by importing the necessary libraries for this lab. We will use scikit-learn to create synthetic datasets, MLPClassifier to build the MLP model, StandardScaler to standardize the data, and make_pipeline to create a pipeline of transformations and classifier.

```python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
```

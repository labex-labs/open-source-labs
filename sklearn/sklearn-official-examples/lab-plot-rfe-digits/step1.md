# Load the Dataset and Split the Data

First, we will load the digits dataset using the Scikit-Learn library. This dataset consists of 8x8 images of digits from 0 to 9. Each image is represented as an array of 64 features. We will split the data into features and target variables.

```python
from sklearn.datasets import load_digits
digits = load_digits()
X = digits.images.reshape((len(digits.images), -1))
y = digits.target
```



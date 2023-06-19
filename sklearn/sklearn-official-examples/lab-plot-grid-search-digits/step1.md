# Load Data

We will load the digits dataset and flatten the images to vectors. Each image of 8 by 8 pixels needs to be transformed to a vector of 64 pixels. Thus, we will get a final data array of shape `(n_images, n_pixels)`. We will also split the data into a training and a testing set of equal size.

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

n_samples = len(digits.images)
X = digits.images.reshape((n_samples, -1))
y = digits.target == 8

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
```



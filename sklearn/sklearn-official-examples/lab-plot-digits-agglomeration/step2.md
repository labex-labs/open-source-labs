# Load Dataset

In this step, we will load the digits dataset from scikit-learn. This dataset contains images of handwritten digits from 0 to 9.

```python
digits = datasets.load_digits()
images = digits.images
X = np.reshape(images, (len(images), -1))
```



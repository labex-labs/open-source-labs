# Dataset laden

In diesem Schritt werden wir das Digits-Dataset aus scikit-learn laden. Dieses Dataset enthält Bilder von handschriftlichen Ziffern von 0 bis 9.

```python
digits = datasets.load_digits()
images = digits.images
X = np.reshape(images, (len(images), -1))
```
